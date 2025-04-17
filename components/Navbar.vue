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


      <hr/>
      <strong>
        <NuxtLink to="/"  class="flex items-center">
          Accueil
        </NuxtLink>
      </strong>

      <hr/>
      <strong>
        <NuxtLink to="/about"  class="flex items-center">
          A propos
        </NuxtLink>
      </strong>

      <hr/>
      <strong> Collection </strong>
      <hr/>

      <UNavigationMenu
        :items="items"
        class="w-full justify-center"
        orientation="vertical"
      />
      <hr/>
    </template>
  </USlideover>
</template>
