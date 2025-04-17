export default defineNuxtConfig({
  target: 'static',
  ssr: false,
  site: {
    url: 'https://arthursonzogni.github.io',
  },
  app: {
    baseURL: '/jewels-collab/',
    pageTransition: { name: 'page', mode: 'out-in' },
  },
  compatibilityDate: '2025-01-01',
  devtools: { enabled: true },
  modules: [
    '@nuxt/content',
    '@nuxt/ui',
    '@nuxt/fonts',
  ],
  css: ['assets/css/main.css'],
  content: {
    build: {
      markdown: {
        toc: {
          depth: 3, // include h3 headings
        },
        highlight: {
          // Theme used in all color schemes.
          theme: 'github-light',
        }
      }
    },
  },
  ui: {
    colorMode: false,
  },
})
