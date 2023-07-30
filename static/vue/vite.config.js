// vite.config.js

import vue from '@vitejs/plugin-vue'

const path = require("path");

// https://vitejs.dev/config/
/** @type {import('vite').UserConfig} */
export default ({ command, mode, ssrBuild }) => ({
    base: command === 'serve' ? '' : '/dist/',
    publicDir: './public',
    build: {
        minify: mode === 'development' ? false : true,
        manifest: true,
        outDir: path.resolve(__dirname, '../dist'),
        rollupOptions: {
            input: './src/main.ts',
        },
    },
    // https://github.com/vuejs/devtools/issues/1330#issuecomment-1337294343
    define: {
        __VUE_PROD_DEVTOOLS__ : mode === 'development' ? true : false,
    },
    plugins: [vue()],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
    },
})
