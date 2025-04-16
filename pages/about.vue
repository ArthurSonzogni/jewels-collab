<template>
  <div class="max-w-4xl mx-auto p-6">
    <Navbar />
    <ContentRenderer :value="document"  class="about p-5" />

    <!-- Button to scroll back to the top -->
    <div class="text-center mt-8">
      <!--<ui-button @click="scrollToTop" variant="primary">Retour en haut</ui-button>-->

      <NuxtLink
        to="/"
        class="text-lg text-gray-700 hover:text-gray-900 dark:text-gray-300
        dark:hover:text-white ml-4"
        >
        Accueil
      </NuxtLink>

      <NuxtLink
        @click="scrollToTop"
        class="text-lg text-gray-700 hover:text-gray-900 dark:text-gray-300
        dark:hover:text-white ml-4"
        >
        Retour en haut
      </NuxtLink>

    </div>
  </div>
</template>

<script lang="ts" setup>

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const { data: document } = await useAsyncData(() =>
  queryCollection('content').path('/about').first()
);

</script>
