<template>
  <div class="collection relative h-screen bg-black text-white">
    <div class="backgroundImage backgroundImageBlur"</div>
    <div class="backgroundImage"</div>
    
    <h1 class="title">Collection Argent</h1>

    <NuxtLink to="/product/necklace-silver" class="link link-1"/>
    <NuxtLink to="/product/earring-silver" class="link link-2"/>
    <NuxtLink to="/product/ring-silver" class="link link-3"/>
    <NuxtLink to="/product/ring-silver" class="link link-4"/>
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
  background-image: url('/images/background-silver.png');
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

.link {
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
  height: 26svh;
  width: 26svh;
  top: 20svh;
  left: calc(50svw + 1svh);
  @media (max-aspect-ratio: 1024/1536) {
    width:30svw;
    height:30svw;
    top: calc(50svh - 40svw);
    left: 56svw;
  }
}

.link-2 {
  height: 26svh;
  width: 26svh;
  top: 43svh;
  left: calc(50svw - 28svh);

  @media (max-aspect-ratio: 1024/1536) {
    width:30svw;
    height:30svw;
    top: calc(50svh - 7svw);
    left: 12svw;
  }
}

.link-3 {
  height: 26svh;
  width: 26svh;
  top: 53svh;
  left: calc(50svw + 1svh);

  @media (max-aspect-ratio: 1024/1536) {
    width:30svw;
    height:30svw;
    top: calc(50svh + 10svw);
    left: 55svw;
  }
}

.link-4 {
  height: 26svh;
  width: 26svh;
  top: 66svh;
  left: calc(50svw - 20svh);

  @media (max-aspect-ratio: 1024/1536) {
    width:30svw;
    height:30svw;
    top: calc(50svh + 25svw);
    left: 24svw;
  }
}

</style>
