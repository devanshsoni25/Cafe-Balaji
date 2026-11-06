import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // Expose on local Wi-Fi network (e.g. http://192.168.1.107:5173/)
    port: 5173,
  },
})
