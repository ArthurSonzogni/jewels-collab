<template>
  <div class="collection relative h-screen bg-black text-white">
    <div class="backgroundImage backgroundImageBlur"</div>
    <div class="backgroundImage"</div>
    
    <div class="absolute inset-0 flex flex-col items-center m-5">
      <h1 class="title">Collection Or</h1>
    </div>

    <NuxtLink to="/product/ring-gold" class="link-1">
    </NuxtLink>
    <NuxtLink to="/product/earring-gold" class="link-2">
    </NuxtLink>
  </div>
</template>

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

.backgroundImage {
  position: absolute;
  top: 0;
  width: 100%;
  background-image: url('/images/background-gold.png');
  background-size: contain;
  background-position: center;
  height: 100lvh;
  background-repeat: no-repeat;

}

.backgroundImageBlur {
  filter: blur(32px);
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

.link-1, .link-2 {
  display: block;
  border-radius: 50%;
  transition: all 1.0s ease;
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
    filter: blur(20px);
  }
  position:absolute;
}

.link-1 {
  height: 26lvh;
  width: 26lvh;
  top: 60lvh;
  left: calc(50lvw - 25lvh);
  @media (max-aspect-ratio: 1024/1792) {
    width:30lvw;
    height:30lvw;
    top: calc(50lvh + 15lvw);
    left: 18lvw;
  }
}

.link-2 {
  height: 26lvh;
  width: 26lvh;
  top: 63lvh;
  left: calc(50lvw + 1lvh);

  @media (max-aspect-ratio: 1024/1792) {
    width:30lvw;
    height:30lvw;
    top: calc(50lvh + 22lvw);
    left: 52lvw;
  }
}

</style>
