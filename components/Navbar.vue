<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

const { data: products } = await useAsyncData(() =>
  queryCollection('products').all()
);

const items = ref<NavigationMenuItem[]>([
  {
    label: 'Jewelry',
    icon: 'i-lucide-diamond',
    to: '/products',
    children: products.value.map((product) => ({
      label: product.title,
      icon: 'i-lucide-file-text',
      description: product.meta.short_description,
      to: `${product.slug}`
    }))
  },
])

console.log(products.value);
console.log(home.value);

</script>

<template>

  <USlideover
    :title="home.title"
    :description="home.description"
    side="left"
  >
    <!--An hamburger icon to open the menu-->
    <UButton
      variant="text"
      class="absolute top-4 left-4 z-10 text-white"

      >
        <UIcon name="i-lucide-menu" class="size-5" />
    </UButton>

    <template #body>
      <UNavigationMenu
        :items="items"
        class="w-full justify-center"
        orientation="vertical"
      />
    </template>
  </USlideover>
</template>

