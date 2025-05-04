<template>
  <div>
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

  </div>


  <div class="max-w-6xl mx-auto p-6 mt-20">
    <div class="products-list">
      <div v-for="(product, index) in allProducts" :key="index"
           class="products"
           >
           <NuxtLink :to="product.path"> 
           <img class="miniature mx-auto"
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

  <div class="lg:max-w-6xl lg:mx-auto lg:p-6">
    <!--Iterate over the models images: collection.meta.images into a nuxt/ui
      UCarousel component.-->
      <UCarousel
        v-slot="{ item }"
        orientation="horizontal"
        :items="collection.meta.images"
        class="carousel mx-auto cover-image"
        :autoplay="{ delay: 4000 }"
        :ui="{ item: 'lg:basis-1/3 md:basis-1/2 sd:basis-full' }"
        >
        <img
          v-if="item.image"
          :key="index"
          :src="`${config.app.baseURL}${item.image}`"
          class="rounded-lg"
          />
      </UCarousel>
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
.products {
  padding: 20px 0;
}

.products-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

.products {
  --width: 300px;
  max-width: var(--width);
  margin: 20px;
}

.miniature {
  width: var(--width);
  height: var(--width);
  object-fit: cover;
  border-radius: 10px;
}

.cover-image {
  width: 100%;
  height: 30lvh;
  object-fit: cover;
}

.carousel {
  padding-bottom: 20px;
  margin-bottom: 20px;
}

</style>
