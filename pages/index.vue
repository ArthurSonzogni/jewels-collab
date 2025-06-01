<script setup lang="ts">
const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

// Format is:
// title: Jewels-Collab
// videos:
//   - title: "Gold Forest"
//     landscape: /videos/gold-forest.mp4
//     portrait: /videos/gold-forest-portrait.mp4
//   - title: "Silver Forest"
//     landscape: /videos/silver-forest.mp4
// images:
//   - image: /images/gold-forest.png
//     link: /collection/gold
//   - image: /images/background-silver.png
//     link: /collection/silver
//   - image: /images/background-gold.png
//     link: /collection/gold

const items = ref(home.value?.meta.videos);

useSeoMeta({
  title: home.value?.title,
  description: home.value?.description
})

const currentVideo = ref(1);

const nextVideo = () => {
  currentVideo.value = (currentVideo.value + 1) % items.length;
};

const prevVideo = () => {
  currentVideo.value = (currentVideo.value - 1 + items.length) % items.length;
};

const images = ref(home.value?.meta.images);

// Resolve the image[i].link with the base URL.
//const origin = window.location.origin;
//for (let i = 0; i < images.value.length; i++) {
//  images.value[i].link = new URL(images.value[i].link, origin).href;
//}


</script>

<template>

  <div>
  <SeeBelow />
  <UCarousel
    v-slot="{ item }"
    orientation="horizontal"
    :items="items"
    dots
    :autoplay="{ delay: 3000 }"
  >
    <div class="video-title">
      {{ item.title }}
    </div>
    <div class="video-container">
      <video
        autoplay
        preload="auto"
        playsinline
        webkit-playsinline
        autoscroll
        loop
        muted
        :src="item.landscape"
        class="background-video"
      >
        <source :src="item.portrait" media="(orientation: portrait)" />
        <source :src="item.landscape" media="(orientation: landscape)" />
      </video>
    </div>
  </UCarousel>
  
  <!--Display the images in 100vh with a link.-->
  <div class="image-collection">
    <div v-for="(image, index) in images" :key="index" class="image-item">
      <NuxtLink :to="image.link">
        <ImageFullscreen
          :image="image.image"
          :title="home.value?.title"
        />
      </NuxtLink>
    </div>
  </div>

  </div>

</template>

<style scoped>
.header h1 {
  font-size: 32px;
  margin-bottom: 20px;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}

.video-container {
  position: relative;
  width: 100svw;
  height: 100svh;
  overflow: hidden;
}

.video-title {
  bottom: 0;
  color: white;
  font-size: 24px;
  font-weight: bold;
  margin-top: 20px;
  position:absolute;
  text-align: center;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
  width: 100%;
  z-index: 1;
}

.background-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.controls {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.control-btn {
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

</style>
