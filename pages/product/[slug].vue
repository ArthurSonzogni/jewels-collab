<template>
  <Navbar />

  <div class="main-container">
    <div class="images">
      <img class="image"
        v-for="(image, index) in product.meta.images"
        :key="index"
        :src="`${config.app.baseURL}${image.image}`"
      />
    </div>

    <div class="details">
      <div class="details-content">
        <h1 class="title font-title">{{ product.title }}</h1>
        <p class="price">{{ product.meta.price }}</p>
        <div class="description">
          <hr />
          <p>{{ product.description }}</p>
        </div>
        <hr />

        <UButton
          v-if="product.meta.payment_link"
          :href="product.meta.payment_link"
          color="neutral"
          variant="soft"
          size="xl"
          icon="fa6-solid:basket-shopping"
        >
          Acheter
        </UButton>

        <br />
      </div>
    </div>
  </div>

  <div class="container">
    <ContentRenderer
      class="markdown p-5"
      :value="product"
      >
    </ContentRenderer>
  </div>

  <template v-for="[title, products] in [
    ['Collection', collection],
    ['Variations', variations],
    ['Vous pouvez aussi aimer', otherProducts]
    ].filter(([_, products]) => products.length > 0)
  ">
    <hr />

    <div class="container">
      <h1 class="other-product title font-title">{{title}}</h1>
      <div class="other-products-list">
        <div
          v-for="(product, index) in products"
          :key="index"
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

</template>

<script setup lang="ts">

const config = useRuntimeConfig();

const slug = useRoute().params.slug;
const { data: product } = await useAsyncData(async () => {
  return await queryCollection('product').path(`/product/${slug}`).first();
});

const { data: allProducts } = await useAsyncData(() =>
  queryCollection('product').all()
);

const variations = allProducts.value
  .filter(p => p.meta.group == product.value.meta.group)
  .filter(p => p.path != product.value.path);

const collection = allProducts.value
  .filter(p => p.meta.collection == product.value.meta.collection)

const otherProducts = allProducts.value
  .filter(p => p.meta.group != product.value.meta.group)
  .filter(p => p.meta.collection != product.value.meta.collection)

useSeoMeta({
  title: product.value.title,
  description: product.value.description,
});
</script>

<style scoped lang="scss">

html {
  scroll-behavior: smooth;
  box-sizing: border-box;
}

.container {
  margin: 0 auto;
}

.main-container {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  flex-wrap: nowrap;
  width: 100vw;

  @media (min-width: 800px) {
    flex-direction: row;
  }
  @media (max-width: 800px) {
    flex-direction: column;
  }
}

.images {
  display: flex;
  background-color: red;
  justify-content: center;
  flex-direction: column;
  margin-right: 20px;
  @media (min-width: 800px) {
    width: 50vw;
  }
  @media (max-width: 800px) {
    width: 100vw;
  }
}

.image {
  width: 100%;
}

// The content stick to the top of the screen.
.details {
  @media (min-width: 800px) {
    width: 50vw;
  }
  @media (max-width: 800px) {
    width: 100vw;
    position:sticky;
    bottom: 0;
    background-color: white;
  }
}

.details-content {
  margin: 20px;
  @media (min-width: 800px) {
    position: sticky;
    top: 50%;
    transform: translateY(-50%);
  }
  @media (max-width: 800px) {
    text-align: center;
  }
}

.title {
  font-weight: bold;
}


pre {
  overflow: scroll;
}

hr {
  margin: 20px 0;
  color: rgba(0, 0, 0, 0.1);
}

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

.description {
  @media (max-width: 800px) {
    display: none;
  }
}

</style>
