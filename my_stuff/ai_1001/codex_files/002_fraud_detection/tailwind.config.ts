import type { Config } from 'tailwindcss';

export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        canvas: '#04131d',
        ink: '#081b27',
        frost: '#ebf4ff',
        accent: '#4ad6c2',
        warning: '#ff9a4d',
        success: '#6df7a0',
        finance: '#7cd0ff',
      },
      boxShadow: {
        chrome: '0 18px 50px rgba(2, 10, 18, 0.32)',
      },
      backgroundImage: {
        aurora:
          'radial-gradient(circle at top left, rgba(74, 214, 194, 0.22), transparent 32%), radial-gradient(circle at top right, rgba(124, 208, 255, 0.18), transparent 28%), linear-gradient(180deg, #071925 0%, #04131d 38%, #06101a 100%)',
      },
      fontFamily: {
        display: ['"Space Grotesk"', '"Inter"', 'sans-serif'],
        sans: ['"IBM Plex Sans"', '"Inter"', 'sans-serif'],
      },
    },
  },
  plugins: [],
} satisfies Config;
