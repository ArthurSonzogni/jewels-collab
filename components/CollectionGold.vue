<template>
  <div class="collection relative h-screen bg-black text-white">
    <div class="backgroundImage backgroundImageBlur"</div>
    <div class="backgroundImage"</div>
    
    <h1 class="title">Collection Or</h1>

    <NuxtLink to="/product/ring-gold" class="link link-1"/>
    <NuxtLink to="/product/earring-gold" class="link link-2"/>
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
  background-image: url('/images/background-gold.png');
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
  top: 60svh;
  left: calc(50svw - 25svh);
  @media (max-aspect-ratio: 1024/1536) {
    width:30svw;
    height:30svw;
    top: calc(50svh + 15svw);
    left: 18svw;
  }
}

.link-2 {
  height: 26svh;
  width: 26svh;
  top: 63svh;
  left: calc(50svw + 1svh);

  @media (max-aspect-ratio: 1024/1536) {
    width:30svw;
    height:30svw;
    top: calc(50svh + 22svw);
    left: 52svw;
  }
}

</style>
