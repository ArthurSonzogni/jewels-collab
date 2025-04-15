<template>
  <Navbar />

  <div class="main-container">
    <div class="images">
      <img class="image"
        v-for="(image, index) in product.meta.images"
        :key="index"
        :src="image.image"
      />
    </div>

    <div class="details">
      <div class="details-content">
        <h1 class="title font-title">{{ product.title }}</h1>
        <p class="price">{{ product.meta.price }}</p>
        <hr />
        <p class="description">{{ product.description }}</p>
        <hr />

        <UButton
          v-if="product.meta.payment_link"
          :href="product.meta.payment_link"
          class="mt-20"
          color="neutral"
          variant="soft"
          size="xl"
          icon="fa6-solid:basket-shopping"
        >
          Acheter
        </UButton>
      </div>
    </div>
  </div>

  <ContentRenderer
    :value="product"
    class="m-20"
  />

  <hr />

  <div class="container">
    <h1 class="other-product title font-title">Vous pouvez aussi aimer</h1>
    <div class="other-products-list">
      <div
        v-for="(product, index) in otherProducts"
        :key="index"
        class="other-product"
      >
        <NuxtLink :to="product.path"> 
          <img class="other-product-image"
            v-if="product.meta.images[0]"
            :key="index"
            :src="product.meta.images[0].image" />
          <h2>{{ product.title }}</h2>
          <p class="price">{{ product.meta.price }}</p>
        </NuxtLink>
      </div>
    </div>
  </div>


  <code class="mt-20">
    <pre>
    {{
      JSON.stringify(product, null, 2)
    }}
    </pre>
  </code>
</template>

<script setup lang="ts">
const slug = useRoute().params.slug;
const { data: product } = await useAsyncData(async () => {
  return await queryCollection('product').path(`/product/${slug}`).first();
});

const { data: otherProducts } = await useAsyncData(() =>
  queryCollection('product').all()
);

otherProducts.value = otherProducts.value.filter((p) => p.path !==
  product.value.path);

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

  @media (min-width: 1000px) {
    flex-direction: row;
  }
  @media (max-width: 1000px) {
    flex-direction: column;
  }
}

.images {
  display: flex;
  background-color: red;
  justify-content: center;
  flex-direction: column;
  margin-right: 20px;
  @media (min-width: 1000px) {
    width: 50vw;
  }
  @media (max-width: 1000px) {
    width: 100vw;
  }
}

.image {
  width: 100%;
}

// The content stick to the top of the screen.
.details {
  @media (min-width: 1000px) {
    width: 50vw;
  }
  @media (max-width: 1000px) {
    width: 100vw;
    position:sticky;
    bottom: 0;
    background-color: white;
  }
}

.details-content {
  margin: 20px;
  @media (min-width: 1000px) {
    position: sticky;
    top: 50%;
    transform: translateY(-50%);
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

.other-product-image {
  width: var(--width);
  height: var(--width);
  object-fit: cover;
}


</style>
