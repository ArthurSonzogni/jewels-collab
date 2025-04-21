<template>
  <!--<UIcon name="i-lucide-arrow-down" class="size-5" />-->
  <UButton
    class="fixed bottom-16 right-4 z-10 text-white scroller"
    color="neutral"
    icon="i-lucide-arrow-up"
    @click="scrollup"
    />
  <UButton
    class="fixed bottom-4 right-4 z-10 text-white scroller"
    color="neutral"
    icon="i-lucide-arrow-down"
    @click="scrolldown"
    />

</template>

<script setup lang="ts">

const scrollup = () => {
  window.scrollBy({
    top: -window.innerHeight,
    behavior: 'smooth'
  })
}

const scrolldown = () => {
  window.scrollBy({
    top: window.innerHeight,
    behavior: 'smooth'
  })
}

</script>

<style scoped lang="scss">

.scroller {
  position: absolute;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}
</style>

