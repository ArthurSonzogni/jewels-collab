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
  image: {
    type: String,
  },
});

onMounted(() => {
  if (image.value) {
    image.value.style.backgroundImage = `url(${props.image})`;
  }
  if (image_back.value) {
    image_back.value.style.backgroundImage = `url(${props.image})`;
  }
});

</script>

<style scoped lang="scss">

nav {
  text-transform: uppercase;
  font-size: 1.5rem;
  font-family: "Luxurious serifs", sans-serif;
  color: rgba(128, 128, 128, 0.8);
  :hover {
    color: rgba(255, 255, 255, 0.8);
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    transition: color 0.3s ease;
  }
}

.collection {
  position: relative;
}


.title {
  position: absolute;
  top: 0;
  width: 100%;
  text-align: center;
  @media (max-aspect-ratio: 1024/1536) {
    top:calc(50svh - 70svw);
  }
}

.backgroundImage {
  position: absolute;
  top: 0;
  width: 100%;
  background-size: contain;
  background-position: center;
  height: 100svh;
  background-repeat: no-repeat;

}

.backgroundImageBlur {
  filter: blur(10px);
  background-repeat: repeat;
}

.title {
  font-family: "Cormorant Garamond", serif;
  font-size: 4rem;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);

  @media (max-width: 768px) {
    font-size: 3rem;
  }
}
</style>
