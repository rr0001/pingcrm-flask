import { createApp, h } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'
import '@/css/app.css'

type StrOrNum = string | number

declare global {
  interface Window {
    reverseUrl(urlName: string, args?: Record<string, unknown> | StrOrNum | StrOrNum[]): string
  }
}

const routeConfig = {
  install: (app: App, _options: Record<string, unknown>) => {
    app.config.globalProperties.$route = window.reverseUrl
  }
}

createInertiaApp({
  resolve: name => {
    const pages = import.meta.glob('./pages/**/*.vue', { eager: true })
    return pages[`./pages/${name}.vue`]
  },
  setup({ el, App, props, plugin }) {
    const vueApp = createApp({ render: () => h(App, props) })
    vueApp.use(plugin)
    vueApp.use(routeConfig)
    vueApp.mount(el)
  }
})
