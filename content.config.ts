import { defineContentConfig } from '@nuxt/content'
import { defineCollection } from '@nuxt/content'

export default defineContentConfig({
  collections: {
    product: defineCollection({
      type: 'page',
      source: 'product/*.md',
    }),
    content: defineCollection({
      type: 'page',
      source: '**/*.md',
      exclude: ['product/*.md'],
    }),
  }
})
