<template>
  <img class="cover-image"
       v-if="collection.meta.cover_image"
       :src="`${config.app.baseURL}${collection.meta.cover_image}`"
  />
  <div class="max-w-6xl mx-auto p-6 mt-20">
    <!--Display the product.meta.cover_image-->

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

    <!--Iterate over the models images: collection.meta.images-->
    <div class="other-products-list">
      <div v-for="(image, index) in collection.meta.images" :key="index"
        class="other-product"
      >
        <img class="miniature"
             v-if="image.image"
             :key="index"
             :src="`${config.app.baseURL}${image.image}`"
             />
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">

const config = useRuntimeConfig();
const route = useRoute();
const slug = route.params.slug;

// Fetch the collection data.
const collection = ref();
collection.value = 
  (
    await queryCollection('collection').path(`/collection/${slug}`).first()
  )

// Fetch all the products, but filter the one that are in the collection.
const allProducts = ref();
allProducts.value = 
  (
    await queryCollection('product').all()
  )
  .filter((product) => {
    return product.meta.collection === slug;
  })


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

.cover-image {
  width: 100%;
  height: 30lvh;
  object-fit: cover;
}

</style>
