<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

const products = await queryCollection('product').all()
console.log(products);

const items = ref<NavigationMenuItem[]>(
  products.map((product) => ({
    label: product.title,
    icon: 'i-lucide-file-text',
    description: product.meta.short_description,
    to: product.path,
  }))
);

</script>

<template>

  <USlideover
    :title="home.title"
    :description="home.description"
    side="left"
  >
    <!--An hamburger icon to open the menu-->
    <UButton
      class="fixed top-4 left-4 z-10 text-white"
      color="neutral"

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
