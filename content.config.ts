import { defineContentConfig } from '@nuxt/content'
import { defineCollection } from '@nuxt/content'

export default defineContentConfig({
  collections: {
    products: defineCollection({
      type: 'page',
      source: 'products/*.md',
      slug: (entry) => `products/${entry.slug}`
    }),
    content: defineCollection({
      type: 'page',
      source: '**/*.md',
      exclude: ['products/*.md'],
    }),
  }
})
