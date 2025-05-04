<script setup lang="ts">

import { GetCollections } from '/composables/collections';

const open = ref(false);

const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

const collections = await GetCollections();

</script>

<template>

  <USlideover
    side="left"
    v-model:open="open"
    >
    <!--An hamburger icon to open the menu-->
    <UButton
      class="fixed top-4 left-4 z-10 text-white"
      >
      <UIcon name="i-lucide-menu" class="size-5" />
      <span class="menu">
        Menu
      </span>
    </UButton>

    <template #body>

      <hr/>
      <strong>
        <NuxtLink to="/"  class="flex items-center"
                          @click="open = false">
        Accueil
        </NuxtLink>
      </strong>

      <hr/>
      <strong>
        <NuxtLink to="/about"  class="flex items-center"
                               @click="open = false">
        A propos
        </NuxtLink>
      </strong>

      <div>
        <div
          v-for="(collection, index) in Object.values(collections)"
          :key="index"
          >
          <hr/>
          <strong>
            <NuxtLink :to="collection.path" @click="open = false">
            {{ collection.title }}
            </NuxtLink>
          </strong>

          <ul class="ml-2">
            <li
              v-for="(product, index) in collection.products"
              :key="index"
              >
              <NuxtLink :to="product.path" @click="open = false">
              {{ product.title }}
              </NuxtLink>
            </li>
          </ul>

        </div>
      </div>
      <hr/>
    </template>
  </USlideover>
</template>

<style scoped lang="scss">

hr {
  margin: 5px 0;
  border: 5px solid rgba(0, 0, 200, 0.05);
  border-radius: 5px;
}


.menu {
  margin: 0;
  padding: 0;
  overflow: hidden;
  animation: grow 1s ease-in-out forwards;
  animation-timeline: scroll();
  animation-range: 0% 500px;
  width: 50px;
}

@keyframes grow {
  from {
    width: 50px;
    opacity: 1;
  }
  to {
    width: 0px;
    opacity: 0;
  }
}

</style>
