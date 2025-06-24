<script setup lang="ts">
const home = await queryCollection('content').path('/').first();
console.log(home);

const videos = ref(home.meta.videos);

useSeoMeta({
  title: home.title,
  description: home.description
})

const currentVideo = ref(1);

const nextVideo = () => {
  currentVideo.value = (currentVideo.value + 1) % videos.length;
};

const prevVideo = () => {
  currentVideo.value = (currentVideo.value - 1 + videos.length) % videos.length;
};

const images = ref(home.meta.images);

// Resolve the image[i].link with the base URL.
//const origin = window.location.origin;
//for (let i = 0; i < images.value.length; i++) {
//  images.value[i].link = new URL(images.value[i].link, origin).href;
//}


</script>

<template>
  <div>

    <div class="max-w-4xl mx-auto p-6">
      <ContentRenderer :value="home"  class="about p-5" />
    </div>

    <div>
      <SeeBelow />
      <UCarousel
        v-slot="{ item }"
        orientation="horizontal"
        :items="videos"
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

      <div v-for="(image, index) in images" :key="index" class="image-item">
        <NuxtLink :to="image.link">
        <ImageFullscreen
          :image="image.image"
          :title="image.title"
          />
        </NuxtLink>
      </div>

    </div>

  </div>
</template>

<style scoped>
.header h1 {
  text-align: center;
  font-size: 2.5rem;
  font-weight: bold;
  margin-top: 20px;
  color: #333;
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
