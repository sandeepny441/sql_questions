import { useFrame } from '@react-three/fiber';
import { useEffect, useMemo, useRef } from 'react';
import * as THREE from 'three';
import { buildLoanAtlas } from '../../lib/demo-data';
import type { CaughtNote, LoanRecord } from '../../types';

interface InstancedLoanNotesProps {
  loans: LoanRecord[];
  caughtNotes: CaughtNote[];
  magnetPosition: THREE.Vector3;
  vesselOffsetY: number;
}

function toneColor(loan: LoanRecord, note?: CaughtNote) {
  if (note?.reviewStatus === 'fraud') {
    return new THREE.Color('#7ef7ad');
  }

  if (note?.reviewStatus === 'falsePositive') {
    return new THREE.Color('#ffab70');
  }

  if (loan.tone === 'risk') {
    return new THREE.Color('#ffd1b2');
  }

  if (loan.tone === 'clean') {
    return new THREE.Color('#f3fff9');
  }

  return new THREE.Color('#fff7b8');
}

export function InstancedLoanNotes({
  loans,
  caughtNotes,
  magnetPosition,
  vesselOffsetY,
}: InstancedLoanNotesProps) {
  const meshRef = useRef<THREE.InstancedMesh>(null);
  const atlasGeometryRef = useRef<THREE.BoxGeometry>(null);
  const dummy = useMemo(() => new THREE.Object3D(), []);
  const tempVector = useMemo(() => new THREE.Vector3(), []);
  const outward = useMemo(() => new THREE.Vector3(), []);

  const motionSeeds = useMemo(
    () =>
      loans.map((_, index) => {
        const angle = (index / loans.length) * Math.PI * 2;
        const radius = 0.38 + ((index * 0.11) % 1.62);
        return {
          base: new THREE.Vector3(
            Math.cos(angle * 2.4) * radius,
            -1.92 + ((index * 0.17) % 3.9),
            Math.sin(angle * 1.8) * radius * 0.78,
          ),
          rot: new THREE.Euler((index % 7) * 0.18, (index % 9) * 0.27, (index % 11) * 0.13),
          drift: 0.6 + (index % 5) * 0.16,
        };
      }),
    [loans],
  );

  const animatedPositions = useRef(motionSeeds.map((seed) => seed.base.clone()));
  const animatedRotations = useRef(
    motionSeeds.map((seed) => new THREE.Quaternion().setFromEuler(seed.rot)),
  );

  const atlas = useMemo(() => buildLoanAtlas(loans), [loans]);
  const caughtLookup = useMemo(
    () => new Map(caughtNotes.map((note) => [note.loanId, note])),
    [caughtNotes],
  );

  const material = useMemo(() => {
    const nextMaterial = new THREE.MeshStandardMaterial({
      map: atlas.texture,
      roughness: 0.8,
      metalness: 0.02,
      vertexColors: true,
    });

    nextMaterial.onBeforeCompile = (shader) => {
      shader.uniforms.atlasScale = {
        value: new THREE.Vector2(1 / atlas.cols, 1 / atlas.rows),
      };

      shader.vertexShader = shader.vertexShader
        .replace(
          '#include <common>',
          `
          #include <common>
          attribute vec2 atlasOffset;
          varying vec2 vAtlasUv;
          uniform vec2 atlasScale;
          `,
        )
        .replace(
          '#include <uv_vertex>',
          `
          #include <uv_vertex>
          vAtlasUv = uv * atlasScale + atlasOffset;
          `,
        );

      shader.fragmentShader = shader.fragmentShader
        .replace(
          '#include <common>',
          `
          #include <common>
          varying vec2 vAtlasUv;
          `,
        )
        .replace(
          '#include <map_fragment>',
          `
          #ifdef USE_MAP
            vec4 sampledDiffuseColor = texture2D(map, vAtlasUv);
            diffuseColor *= sampledDiffuseColor;
          #endif
          `,
        );
    };

    return nextMaterial;
  }, [atlas.cols, atlas.rows, atlas.texture]);

  useEffect(() => {
    const geometry = atlasGeometryRef.current;

    if (!geometry) {
      return;
    }

    const offsets = new Float32Array(loans.length * 2);
    loans.forEach((loan, index) => {
      const col = loan.atlasIndex % atlas.cols;
      const row = Math.floor(loan.atlasIndex / atlas.cols);
      offsets[index * 2] = col / atlas.cols;
      offsets[index * 2 + 1] = 1 - (row + 1) / atlas.rows;
    });

    geometry.setAttribute('atlasOffset', new THREE.InstancedBufferAttribute(offsets, 2));
  }, [atlas.cols, atlas.rows, loans]);

  useEffect(() => {
    const mesh = meshRef.current;

    if (!mesh) {
      return;
    }

    loans.forEach((loan, index) => {
      const caught = caughtLookup.get(loan.id);
      mesh.setColorAt(index, toneColor(loan, caught));
    });

    mesh.instanceColor!.needsUpdate = true;
  }, [caughtLookup, loans]);

  useFrame((state, delta) => {
    const mesh = meshRef.current;

    if (!mesh) {
      return;
    }

    loans.forEach((loan, index) => {
      const seed = motionSeeds[index];
      const caught = caughtLookup.get(loan.id);
      const position = animatedPositions.current[index];
      const rotation = animatedRotations.current[index];

      if (caught) {
        tempVector.set(
          magnetPosition.x + caught.slot[0],
          magnetPosition.y - vesselOffsetY + caught.slot[1],
          magnetPosition.z + caught.slot[2],
        );
        position.lerp(tempVector, 1 - Math.exp(-delta * 5.4));

        outward.set(caught.slot[0], caught.slot[1], caught.slot[2]).normalize();
        dummy.position.copy(position);
        dummy.lookAt(position.clone().add(outward));
        dummy.rotateY(Math.PI);
        rotation.slerp(dummy.quaternion, 1 - Math.exp(-delta * 7));
      } else {
        tempVector.copy(seed.base);
        tempVector.x += Math.sin(state.clock.elapsedTime * seed.drift + index * 0.23) * 0.18;
        tempVector.y += Math.sin(state.clock.elapsedTime * (seed.drift + 0.35) + index * 0.11) * 0.09;
        tempVector.z += Math.cos(state.clock.elapsedTime * (seed.drift + 0.2) + index * 0.17) * 0.16;

        position.lerp(tempVector, 1 - Math.exp(-delta * 1.8));
        dummy.quaternion.setFromEuler(
          new THREE.Euler(
            seed.rot.x + Math.sin(state.clock.elapsedTime + index) * 0.08,
            seed.rot.y + Math.cos(state.clock.elapsedTime * 0.8 + index) * 0.12,
            seed.rot.z + Math.sin(state.clock.elapsedTime * 0.65 + index) * 0.08,
          ),
        );
        rotation.slerp(dummy.quaternion, 1 - Math.exp(-delta * 2.2));
        dummy.position.copy(position);
      }

      dummy.quaternion.copy(rotation);
      dummy.scale.set(0.6, 0.46, 0.05);
      dummy.updateMatrix();
      mesh.setMatrixAt(index, dummy.matrix);
    });

    mesh.instanceMatrix.needsUpdate = true;
  });

  return (
    <instancedMesh ref={meshRef} args={[undefined, undefined, loans.length]} castShadow receiveShadow>
      <boxGeometry ref={atlasGeometryRef} args={[1, 1, 0.08]} />
      <primitive object={material} attach="material" />
    </instancedMesh>
  );
}
