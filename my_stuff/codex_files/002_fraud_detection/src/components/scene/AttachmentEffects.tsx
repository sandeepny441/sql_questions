import { useFrame } from '@react-three/fiber';
import { useRef } from 'react';
import * as THREE from 'three';
import type { CaughtNote } from '../../types';

interface AttachmentEffectsProps {
  caughtNotes: CaughtNote[];
  magnetPosition: THREE.Vector3;
}

function Pulse({
  position,
  color,
  startedAt,
}: {
  position: [number, number, number];
  color: string;
  startedAt: number;
}) {
  const ref = useRef<THREE.Mesh>(null);

  useFrame(() => {
    if (!ref.current) {
      return;
    }

    const age = (performance.now() - startedAt) / 1000;
    const scale = 0.35 + Math.min(age, 1.4) * 1.7;
    ref.current.scale.setScalar(scale);
    (ref.current.material as THREE.MeshBasicMaterial).opacity = Math.max(0, 0.26 - age * 0.18);
  });

  return (
    <mesh ref={ref} position={position}>
      <sphereGeometry args={[0.18, 16, 16]} />
      <meshBasicMaterial color={color} transparent opacity={0.24} />
    </mesh>
  );
}

export function AttachmentEffects({ caughtNotes, magnetPosition }: AttachmentEffectsProps) {
  const now = performance.now();
  const recentNotes = caughtNotes.filter((note) => now - note.attachedAt < 2200);

  return (
    <group>
      {caughtNotes.map((note) => {
        const color = note.reviewStatus === 'fraud' ? '#6df7a0' : '#ff9a4d';
        const position: [number, number, number] = [
          magnetPosition.x + note.slot[0],
          magnetPosition.y + note.slot[1],
          magnetPosition.z + note.slot[2],
        ];

        return (
          <mesh key={note.loanId} position={position}>
            <sphereGeometry args={[0.16, 14, 14]} />
            <meshBasicMaterial color={color} transparent opacity={0.2} />
          </mesh>
        );
      })}

      {recentNotes.map((note) => {
        const color = note.reviewStatus === 'fraud' ? '#6df7a0' : '#ff9a4d';
        const position: [number, number, number] = [
          magnetPosition.x + note.slot[0],
          magnetPosition.y + note.slot[1],
          magnetPosition.z + note.slot[2],
        ];

        return (
          <Pulse
            key={`${note.loanId}-pulse`}
            position={position}
            color={color}
            startedAt={note.attachedAt}
          />
        );
      })}
    </group>
  );
}
