<template>
  <div>
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
          <div class="small_screen">
            <div>
              <span class="title mr-6">{{ product.title }}</span>
              <span class="price">{{ product.meta.price }}</span>
            </div>
            <UButton
              v-if="product.meta.payment_link"
              :href="product.meta.payment_link"
              icon="fa6-solid:basket-shopping"
              color="primary"
              variant="soft"
              class="mt-4"
              >
              Acheter
            </UButton>
          </div>

          <div class="large_screen">
            <h1 class="title font-title mr-6">{{ product.title }}</h1>
            <span class="price">{{ product.meta.price }}</span>
            <hr />
            <p>{{ product.description }}</p>
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
          </div>
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

    <template v-for="[title, products] in collections_list">
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
  </div>
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

// Fetch all the collections and map the collection.slug to its collection.title
const { data: collections_data } = await useAsyncData(() =>
  queryCollection('collection').all()
);

const collection_titles = new Map();
collections_data.value.forEach(collection => {
  console.log(collection)
  collection_titles.set(collection.meta.slug, collection.title);
});
console.log(collection_titles);

// Fetch all products, and group by collection. Extract the collection from the
// first product alone.

const collections = {};
allProducts.value.forEach(product => {
  collections[product.meta.collection] ||= [];
  collections[product.meta.collection].push(product);
});

const collection_current = collections[product.value.meta.collection];
delete collections[product.value.meta.collection];

// Turn the [collection_current, collections...] into a list of [title, products]
// where title is the collection name, and products is the list of products.

const collections_list = [
  [product.value.meta.collection, collection_current],
  ...Object.entries(collections)
    .filter(([title, products]) => products.length > 0)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([title, products]) => [collection_titles.get(title), products])
]

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
  @media (min-width: 800px) {
    width: 50vw;
  }
  @media (max-width: 800px) {
    width: 100vw;
  }
}

.image {
  width: 100%;

  @media (max-width: 800px) {
    width: 100vw;
  }
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

.large_screen{
  @media (max-width: 800px) {
    display: none;
  }
}

.small_screen{
  @media (min-width: 800px) {
    display: none;
  }
}

</style>
