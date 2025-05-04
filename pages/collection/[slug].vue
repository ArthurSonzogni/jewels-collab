<template>
  <div class="max-w-6xl mx-auto p-6 mt-20">

    <h1 class="title font-title">
      {{ collection.title }}
    </h1>

    <p class="description">
      {{ collection.description }}
    </p>

    <div class="other-products-list">
      <div v-for="(product, index) in allProducts" :key="index"
        class="other-product"
      >
        <NuxtLink :to="product.path"> 
        <img class="miniature"
             v-if="product.meta.images[0]"
             :key="index"
             :src="`${config.app.baseURL}${product.meta.images[0].image}`"
             />
        <h2>{{ product.title }}</h2>
        <p class="price">{{ product.meta.price }}</p>
        </NuxtLink>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">

const config = useRuntimeConfig();

const slug = useRoute().params.slug;

// Fetch the collection data.
const { data: collection } = await useAsyncData(() =>
  queryCollection('collection').path(`/collection/${slug}`).first()
);

// Fetch all the products, but filter the one that are in the collection.
const { data: allProducts } = await useAsyncData(() =>
  queryCollection('product').all()
);

// Filter out the products that are not in the collection.
allProducts.value = allProducts.value.filter((product) => {
  return product.meta.collection === slug;
});


</script>


<style scoped lang="scss">
.other-product {
  padding: 20px 0;
}

.other-products-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

.other-product {
  --width: 300px;
  max-width: var(--width);
  margin: 20px;
}

.miniature {
  width: var(--width);
  height: var(--width);
  object-fit: cover;
}
</style>
