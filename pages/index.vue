<template>
  <div class="relative h-screen bg-black text-white">
    <Navbar />

    <div class="absolute inset-0 backgroundImageBlur"</div>
    <div class="absolute inset-0 backgroundImage"</div>
    
    <!-- Contenu superposé -->
    <div class="absolute inset-0 flex flex-col items-center m-5">
      <!-- Menu -->
      <nav class="top-5 left-5 right-5 flex justify-center items-center gap-10">
        <NuxtLink class="navLink" to="/collection" >Collection</NuxtLink>
        <NuxtLink class="navLink" to="/about" >A propos</NuxtLink>
      </nav>

      <!-- Titre -->
      <h1 class="title">Jewels Collab</h1>

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

.backgroundImage {
  background-image: url('/images/background-gold.png');
  background-size: contain;
  background-position: center;
  height: 100lvh;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
.backgroundImageBlur {
  background-image: url('/images/background-gold.png');
  background-size: contain;
  background-position: center;
  height: 100lvh;
  background-attachment: fixed;
  filter: blur(32px)
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

// Transparent link that should fit the position of the jewel in the background.
.link-1 {
  display: block;
  border-radius: 50%;
  transition: background-color 1.0s ease;
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }

  position:absolute;

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
  position:absolute;

  border-radius: 50%;
  transition: background-color 1.0s ease;
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }

  height: 26lvh;
  width: 26lvh;
  top: 63lvh;
  left: calc(50lvw + 1lvh);

  @media (max-aspect-ratio: 1024/1792) {
    width:30lvw;
    height:30lvw;
    top: calc(50lvh + 20lvw);
    left: 52lvw;
  }
}


</style>
