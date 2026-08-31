import { MeshTransmissionMaterial } from '@react-three/drei';

export function Bottle() {
  return (
    <group position={[0, 0.2, 0]}>
      <mesh castShadow receiveShadow position={[0, 0.15, 0]}>
        <cylinderGeometry args={[2.35, 2.75, 5.15, 72, 1, true]} />
        <MeshTransmissionMaterial
          backside
          samples={6}
          resolution={256}
          transmission={1}
          thickness={0.95}
          roughness={0.05}
          ior={1.18}
          chromaticAberration={0.015}
          color="#e8f7ff"
        />
      </mesh>

      <mesh position={[0, 2.88, 0]} rotation={[Math.PI / 2, 0, 0]}>
        <torusGeometry args={[2.37, 0.1, 24, 100]} />
        <meshPhysicalMaterial color="#eefaff" metalness={0.04} roughness={0.15} />
      </mesh>

      <mesh position={[0, -2.42, 0]} rotation={[Math.PI / 2, 0, 0]}>
        <cylinderGeometry args={[2.72, 2.48, 0.42, 72]} />
        <meshPhysicalMaterial color="#effbff" transmission={0.65} transparent opacity={0.28} roughness={0.18} />
      </mesh>

      <mesh position={[0, -0.1, 0]}>
        <cylinderGeometry args={[2.14, 2.36, 4.25, 64]} />
        <meshPhysicalMaterial color="#9cc9d9" transparent opacity={0.05} roughness={0.22} />
      </mesh>

      <mesh position={[0, -2.53, 0]} rotation={[Math.PI / 2, 0, 0]}>
        <circleGeometry args={[2.3, 72]} />
        <meshPhysicalMaterial color="#d7eef6" transparent opacity={0.18} roughness={0.2} />
      </mesh>
    </group>
  );
}
