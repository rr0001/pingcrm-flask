// vite.config.js

import vue from '@vitejs/plugin-vue'

const path = require("path");

// https://vitejs.dev/config/
export default ({ command }) => ({
    base: command === 'serve' ? '' : '/dist/',
    publicDir: './public',
    build: {
        manifest: true,
        outDir: path.resolve(__dirname, '../dist'),
        rollupOptions: {
            input: './src/main.ts',
        },
    },
    plugins: [vue()],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
    },
})
