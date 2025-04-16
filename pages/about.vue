<template>
  <div class="max-w-4xl mx-auto p-6">
    <h1 class="text-4xl font-extrabold text-center mb-6">À propos de Vincent Arnould</h1>
    
    <!-- Render markdown content using ContentRenderer -->
    <div v-if="document" class="prose lg:prose-xl">
      <ContentRenderer :value="document"  class="markdown p-5" />
    </div>

    <!-- Button to scroll back to the top -->
    <div class="text-center mt-8">
      <ui-button @click="scrollToTop" variant="primary">Retour en haut</ui-button>
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

console.log(document.value);

</script>

<style scoped lang="scss">

.markdown {
  font-family: "Cormorant Garamond", serif;

  a {
    color: #000;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}

</style>

