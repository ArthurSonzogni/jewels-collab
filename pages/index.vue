<script setup lang="ts">
const { data: home } = await useAsyncData(() =>
  queryCollection('content').path('/').first()
);

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


</script>

<template>
  <Navbar />

  <UCarousel
    v-slot="{ item }"
    orientation="horizontal"
    :items="items"
    dots
    :autoplay="{ delay: 3000 }"
  >
    <div class="video-container">
    <video
      preload="auto"
      playsinline
      webkit-playsinline
      autoplay
      muted
      :src="item.landscape"
      class="background-video"
    >
      coucou
      <source :src="item.portrait" media="(orientation: portrait)" />
      <source :src="item.landscape" media="(orientation: landscape)" />
    </video>
    </div>
  </UCarousel>

  <div class="container1">
    <header class="header">
      <h1>
        {{ home?.title }}
      </h1>
    </header>

  </div>
  <div class="container3">
  </div>
  <div class="container2">
  </div>

</template>

<style scoped>
.container1 {
  background: #000 url('/images/background_1.png') no-repeat center center;
  background-size: contain;
  color: white;
  height: 100vh;
  width: 100vw;
  padding: 40px;
  text-align: center;
  font-family: 'Times New Roman', serif;
}

.container2 {
  border-top: 2px dashed white;
  background:
    #000
    url('/images/background_2.png') no-repeat center center;
  background-size: contain;
  color: white;
  height: 100vh;
  width: 100vw;
  padding: 40px;
  text-align: center;
  font-family: 'Times New Roman', serif;
}

.container3 {
  border-top: 2px dashed white;
  background:
    #000
    url('/images/background_3.png') no-repeat center center;
  background-size: contain;
  color: white;
  height: 100vh;
  width: 100vw;
  padding: 40px;
  text-align: center;
  font-family: 'Times New Roman', serif;
}

.header h1 {
  font-size: 32px;
  margin-bottom: 20px;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.card {
  background-color: rgba(34, 34, 34, 0.8);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
}

.image {
  width: 100%;
  max-width: 200px;
  border-radius: 4px;
}

.title {
  font-size: 20px;
  margin-top: 10px;
}

.price {
  font-size: 18px;
  color: gold;
  margin-top: 5px;
}

.video-container {
  position: relative;
  width: 100vw;
  height: calc(100vh - 100px);
  overflow: hidden;
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
  padding: 20px;
}

.control-btn {
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 24px;
  cursor: pointer;
}

.overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  text-align: center;
}

.title {
  font-size: 36px;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}
</style>
