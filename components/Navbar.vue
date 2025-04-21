<script setup lang="ts">

const open = ref(false);

const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

const products = await queryCollection('product').all()

</script>

<template>

  <USlideover
    side="left"
    v-model:open="open"
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

      <hr/>
      <strong> Collection </strong>
      <hr/>

      <div class="flex flex-col gap-2">
        <div
          v-for="(product, index) in products"
          :key="index"
          class="flex items-center gap-2"
          >
          <NuxtLink :to="product.path" @click="open = false">
            {{ product.title }}
          </NuxtLink>
        </div>
      </div>

      <hr/>
    </template>
  </USlideover>
</template>
