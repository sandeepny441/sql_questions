# Fraud Magnet - Mortgage Fraud Detection Demo

Run locally:

```bash
npm install
npm run dev
```

Build for production:

```bash
npm run build
```

Project structure:

```text
fraud_detection/
  index.html
  package.json
  postcss.config.cjs
  tailwind.config.ts
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
  src/
    App.tsx
    index.css
    main.tsx
    types.ts
    lib/
      demo-data.ts
      format.ts
    components/
      MagnetDemo.tsx
      SidebarPanel.tsx
      scene/
        AttachmentEffects.tsx
        Bottle.tsx
        FraudScene.tsx
        InstancedLoanNotes.tsx
```

This demo uses React Three Fiber for the 3D bottle scene, Tailwind CSS for the dashboard, and seeded fake mortgage loan data so the animation is stable and pitch-ready every time you reload.
