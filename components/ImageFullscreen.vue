<template>
  <div class="collection relative h-screen bg-black text-white">
    <div ref="image" class="backgroundImage backgroundImageBlur"</div>
    <div ref="image_back" class="backgroundImage"</div>
    
    <h1 class="title">
      {{ props.title }}
    </h1>
  </div>
</template>

<script setup lang="ts">

const image = ref<HTMLDivElement | null>(null);
const image_back = ref<HTMLDivElement | null>(null);

const props = defineProps({
  title: {
    type: String,
  },
  image_portrait: {
    type: String,
  },
  image_landscape: {
    type: String,
  },
});

onMounted(() => {
  if (image.value) {
    image.value.style.setProperty('--background-image-portrait', `url(${props.image_portrait})`);
    image.value.style.setProperty('--background-image-landscape', `url(${props.image_landscape})`);
  }
  if (image_back.value) {
    image_back.value.style.setProperty('--background-image-portrait', `url(${props.image_portrait})`);
    image_back.value.style.setProperty('--background-image-landscape', `url(${props.image_landscape})`);
  }
});

</script>

<style scoped lang="scss">

@keyframes blur-text {
  0% {
    filter: blur(0);
  }

  100% {
    filter: blur(30px);
  }
}

.collection {
  position: relative;
}

.title {
  position: absolute;
  bottom: 3rem;
  width: 100%;
  text-align: center;
  @media (max-aspect-ratio: 1024/1536) {
    bottom:calc(50svh - 70svw);
  }
}

.backgroundImage {
  position: absolute;
  top: 0;
  width: 100%;
  background-size: cover;
  background-position: center;
  height: 100svh;
  background-repeat: no-repeat;
  background-image: var(--background-image-portrait);

  @media (orientation: landscape) {
    background-image: var(--background-image-landscape);
  }
}

.backgroundImageBlur {
  filter: blur(10px);
}

.title {
  font-family: "Cormorant Garamond", serif;
  font-size: 3rem;
  margin-top: 3rem;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);

  animation: blur-text linear forwards;
  animation-timeline: view();
  animation-range: 70% 100%;

  @media (max-width: 768px) {
    margin-top: 2rem;
    font-size: 2rem;
  }
}
</style>
