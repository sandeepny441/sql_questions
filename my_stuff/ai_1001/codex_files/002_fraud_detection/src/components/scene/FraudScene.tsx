import {
  ContactShadows,
  OrbitControls,
  PerspectiveCamera,
  Sparkles,
} from '@react-three/drei';
import { Canvas, ThreeEvent, useFrame, useThree } from '@react-three/fiber';
import { useEffect, useMemo, useRef } from 'react';
import * as THREE from 'three';
import type { OrbitControls as OrbitControlsImpl } from 'three-stdlib';
import type { CaughtNote, LoanRecord } from '../../types';
import { AttachmentEffects } from './AttachmentEffects';
import { Bottle } from './Bottle';
import { InstancedLoanNotes } from './InstancedLoanNotes';

interface FraudSceneProps {
  loans: LoanRecord[];
  caughtNotes: CaughtNote[];
  pullSignal: number;
  resetSignal: number;
  onTriggerMagnet: () => void;
}

function clampMagnetPosition(position: THREE.Vector3) {
  const next = position.clone();
  next.z = 0;
  next.x = THREE.MathUtils.clamp(next.x, -3.2, 3.2);
  next.y = THREE.MathUtils.clamp(next.y, -2.1, 4.9);
  return next;
}

function SceneContents({
  loans,
  caughtNotes,
  pullSignal,
  resetSignal,
  onTriggerMagnet,
}: FraudSceneProps) {
  const { camera, gl, raycaster, pointer } = useThree();
  const orbitRef = useRef<OrbitControlsImpl>(null);
  const dragPlane = useMemo(() => new THREE.Plane(new THREE.Vector3(0, 0, 1), 0), []);
  const intersection = useMemo(() => new THREE.Vector3(), []);
  const magnetPosition = useRef(new THREE.Vector3(2.85, 3.45, 0));
  const magnetTarget = useRef(new THREE.Vector3(2.85, 3.45, 0));
  const magnetMesh = useRef<THREE.Mesh>(null);
  const magnetRing = useRef<THREE.Mesh>(null);
  const dragging = useRef(false);
  const pulledFromBottle = useRef(false);
  const autoRoute = useRef<THREE.Vector3[] | null>(null);
  const autoIndex = useRef(0);
  const didAutoTrigger = useRef(false);
  const vesselOffsetY = 0.2;

  useEffect(() => {
    magnetPosition.current.set(2.85, 3.45, 0);
    magnetTarget.current.set(2.85, 3.45, 0);
    autoRoute.current = null;
    autoIndex.current = 0;
    didAutoTrigger.current = false;
    pulledFromBottle.current = false;
  }, [resetSignal]);

  useEffect(() => {
    autoRoute.current = [
      magnetPosition.current.clone(),
      new THREE.Vector3(1.55, 2.95, 0),
      new THREE.Vector3(0.55, 1.3, 0),
      new THREE.Vector3(0.05, -0.55, 0),
      new THREE.Vector3(0.4, 1.7, 0),
      new THREE.Vector3(1.55, 4.25, 0),
    ];
    autoIndex.current = 1;
    didAutoTrigger.current = false;
    pulledFromBottle.current = true;
  }, [pullSignal]);

  useFrame((_, delta) => {
    if (dragging.current) {
      raycaster.setFromCamera(pointer, camera);
      if (raycaster.ray.intersectPlane(dragPlane, intersection)) {
        magnetTarget.current.copy(clampMagnetPosition(intersection));
      }
    }

    if (autoRoute.current) {
      const target = autoRoute.current[autoIndex.current];
      magnetTarget.current.copy(target);
      magnetPosition.current.lerp(target, 1 - Math.exp(-delta * 3.6));

      if (magnetPosition.current.distanceTo(target) < 0.14) {
        if (autoIndex.current === autoRoute.current.length - 1) {
          if (!didAutoTrigger.current) {
            onTriggerMagnet();
            didAutoTrigger.current = true;
            pulledFromBottle.current = false;
          }
          autoRoute.current = null;
        } else {
          autoIndex.current += 1;
        }
      }
    } else {
      magnetPosition.current.lerp(magnetTarget.current, 1 - Math.exp(-delta * 6));
    }

    if (magnetMesh.current) {
      magnetMesh.current.position.copy(magnetPosition.current);
      magnetMesh.current.rotation.y += delta * 0.5;
    }

    if (magnetRing.current) {
      magnetRing.current.position.copy(magnetPosition.current);
      magnetRing.current.rotation.z += delta * 0.3;
    }

    const insideBottle =
      Math.abs(magnetPosition.current.x) < 1.95 &&
      magnetPosition.current.y > -2.0 &&
      magnetPosition.current.y < 2.25;

    if (insideBottle) {
      pulledFromBottle.current = true;
    }

    if (
      pulledFromBottle.current &&
      magnetPosition.current.y > 3.45 &&
      Math.abs(magnetPosition.current.x) < 2.25 &&
      !dragging.current &&
      !autoRoute.current
    ) {
      onTriggerMagnet();
      pulledFromBottle.current = false;
    }
  });

  const handlePointerDown = (event: ThreeEvent<PointerEvent>) => {
    event.stopPropagation();
    dragging.current = true;
    autoRoute.current = null;
    gl.domElement.style.cursor = 'grabbing';
    if (orbitRef.current) {
      orbitRef.current.enabled = false;
    }
    const pointerTarget = event.target as EventTarget & {
      setPointerCapture?: (pointerId: number) => void;
    };
    pointerTarget.setPointerCapture?.(event.pointerId);
  };

  const handlePointerUp = (event: ThreeEvent<PointerEvent>) => {
    event.stopPropagation();
    dragging.current = false;
    gl.domElement.style.cursor = 'grab';
    if (orbitRef.current) {
      orbitRef.current.enabled = true;
    }
    const pointerTarget = event.target as EventTarget & {
      releasePointerCapture?: (pointerId: number) => void;
    };
    pointerTarget.releasePointerCapture?.(event.pointerId);
  };

  return (
    <>
      <color attach="background" args={['#07141c']} />
      <fog attach="fog" args={['#07141c', 8, 16]} />

      <PerspectiveCamera makeDefault position={[0, 1.4, 8.1]} fov={33} />

      <ambientLight intensity={0.75} color="#deefff" />
      <hemisphereLight intensity={0.55} color="#c3efff" groundColor="#5d4732" />
      <directionalLight
        castShadow
        position={[5, 8, 6]}
        intensity={1.55}
        color="#ffffff"
        shadow-mapSize-width={2048}
        shadow-mapSize-height={2048}
      />
      <spotLight
        position={[-4, 7, 3]}
        angle={0.48}
        penumbra={0.9}
        intensity={55}
        color="#93e6ff"
      />
      <pointLight position={[0, 1.2, 4.2]} intensity={18} color="#8eefff" />
      <pointLight position={[0, -1, -4.5]} intensity={9} color="#8ccfb7" />

      <group position={[0, -2.75, 0]}>
        <mesh rotation={[-Math.PI / 2, 0, 0]} receiveShadow>
          <circleGeometry args={[6.2, 96]} />
          <meshStandardMaterial color="#2a2118" metalness={0.08} roughness={0.9} />
        </mesh>
      </group>

      <mesh position={[0, 1.3, -3.4]}>
        <planeGeometry args={[14, 9]} />
        <meshBasicMaterial color="#0c1a22" transparent opacity={0.55} />
      </mesh>

      <Bottle />

      <group position={[0, 0.2, 0]}>
        <InstancedLoanNotes
          loans={loans}
          caughtNotes={caughtNotes}
          magnetPosition={magnetPosition.current}
          vesselOffsetY={vesselOffsetY}
        />
      </group>

      <group>
        <mesh
          ref={magnetMesh}
          castShadow
          receiveShadow
          position={magnetPosition.current}
          onPointerDown={handlePointerDown}
          onPointerUp={handlePointerUp}
          onPointerOut={() => {
            if (!dragging.current) {
              gl.domElement.style.cursor = 'grab';
            }
          }}
          onPointerOver={() => {
            if (!dragging.current) {
              gl.domElement.style.cursor = 'grab';
            }
          }}
        >
          <sphereGeometry args={[0.66, 56, 56]} />
          <meshPhysicalMaterial
            color="#edf3fb"
            metalness={1}
            roughness={0.16}
            clearcoat={1}
            clearcoatRoughness={0.06}
          />
        </mesh>

        <mesh ref={magnetRing}>
          <torusGeometry args={[0.88, 0.035, 12, 64]} />
          <meshBasicMaterial color="#8de2ff" transparent opacity={0.42} />
        </mesh>
      </group>

      <AttachmentEffects caughtNotes={caughtNotes} magnetPosition={magnetPosition.current} />

      <Sparkles
        count={52}
        scale={[8, 5, 6]}
        position={[0, 1.8, 0]}
        size={2.2}
        speed={0.16}
        opacity={0.24}
        color="#8ef6f4"
      />

      <ContactShadows position={[0, -2.32, 0]} opacity={0.38} blur={2.8} scale={10} far={5.5} />
      <OrbitControls
        ref={orbitRef}
        enablePan={false}
        minDistance={6.8}
        maxDistance={10.5}
        minPolarAngle={0.95}
        maxPolarAngle={1.42}
      />
    </>
  );
}

export function FraudScene(props: FraudSceneProps) {
  return (
    <Canvas shadows dpr={[1, 1.8]}>
      <SceneContents {...props} />
    </Canvas>
  );
}
