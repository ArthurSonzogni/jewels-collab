<template>
  <Navbar />

  <div class="product-container">
    <div class="product-images">
      <img class="product-image"
        v-for="(image, index) in product.meta.images"
        :key="index"
        :src="image.image"
      />
    </div>

    <div class="product-details">
      <div class="product-details-content">
        <h1 class="product-title">{{ product.title }}</h1>
        <hr />
        <p class="product-description">{{ product.meta.long_description }}</p>
        <hr />
        <p class="product-price">{{ product.meta.price }}</p>
        <UButton
          variant="text"
          class="mt-4 p-3 text-lg font-bold font-sans w-full"
          :to="product.meta.payment_link"
          >
          <UIcon name="i-lucide-shopping-cart" class="size-5" />
          <span class="center w-full">Acheter</span>
        </UButton>
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

console.log(product.value);

useSeoMeta({
  title: product.value.title,
  description: product.value.description,
});
</script>

<style scoped>

.product-container {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  align-content: stretch;
  flex-direction: row;
  flex-wrap: nowrap;
}
@media (min-width: 1000px) {
  .product-container {
    flex-direction: row;
  }
}
@media (max-width: 1000px) {
  .product-container {
    flex-direction: column;
  }
}


.product-images {
  display: flex;
  flex-direction: column;
  margin-right: 20px;
}

.product-image {
  width: 100vw;
  max-width: 1000px;
  object-fit: cover;
}

.product-title {
  font-weight: bold;
}


@media (min-width: 1000px) {
  .product-details {
    display: sticky;
    max-width: 500px;
    margin: 0;
    padding: 30px;
  }
  .product-details-content {
    position: sticky;
    top: 50%;
    transform: translateY(-50%);
  }
}
@media (max-width: 1000px) {
  .product-details {
    position: sticky;
    background: white;
    bottom: 0;
    width: 100vw;
    margin: 0;
    padding: 30px;
  }
  .product-details-content {
    top: 0;
    width: 100vw;
  }
}

pre {
  overflow: scroll;
}

hr {
  margin: 20px 0;
  color: rgba(0, 0, 0, 0.1);
}

</style>
