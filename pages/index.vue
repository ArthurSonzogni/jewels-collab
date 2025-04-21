<script setup lang="ts">
const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

const items = ref(home.value?.meta.videos);
console.log(items.value);

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
  
  <CollectionGold />
  <CollectionSilver />

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
  width: 100lvw;
  height: 100lvh;
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
