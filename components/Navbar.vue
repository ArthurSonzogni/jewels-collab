<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

const products = await queryCollection('product').all()

const items = ref<NavigationMenuItem[]>(
  products.map((product) => ({
    label: product.title,
    description: product.meta.short_description,
    to: product.path,
  }))
);

</script>

<template>

  <USlideover
    :title="home.title"
    description="description"
    side="left"
    portal=true
  >
    <!--An hamburger icon to open the menu-->
    <UButton
      class="fixed top-4 left-4 z-10 text-white"
      color="neutral"

      >
        <UIcon name="i-lucide-menu" class="size-5" />
    </UButton>

    <template #header>
      <div class="flex flex-col items-center justify-center h-full">
        <NuxtLink :to="home.path" class="flex items-center">
          <h1 class="text-3xl font-bold text-center">
            {{ home.title }}
          </h1>
        </NuxtLink>
      </div>
    </template>

    <template #body>
      <p>
        {{ home.description }}
      </p>

      <UNavigationMenu
        :items="items"
        class="w-full justify-center"
        orientation="vertical"
      />
    </template>
  </USlideover>
</template>
