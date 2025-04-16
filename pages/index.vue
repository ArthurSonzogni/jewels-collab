<template>
  <div class="relative h-screen bg-black text-white">
    <Navbar />

    <div class="absolute inset-0 backgroundImageBlur"</div>
    <div class="absolute inset-0 backgroundImage"</div>
    
    <!-- Contenu superposé -->
    <div class="absolute inset-0 flex flex-col items-center m-5">
      <!-- Menu -->
      <nav class="top-5 left-5 right-5 flex justify-center items-center gap-10">
        <NuxtLink class="navLink" to="/" >Accueil</NuxtLink>
        <NuxtLink class="navLink" to="/collection" >Collection</NuxtLink>
        <NuxtLink class="navLink" to="/about" >A propos</NuxtLink>
      </nav>

      <!-- Titre -->
      <h1 class="title">Jewels Collab</h1>

    </div>
    <NuxtLink to="/product/ring-gold" class="link-1">
    </NuxtLink>
    <NuxtLink to="/product/ring-gold" class="link-2">
    </NuxtLink>
  </div>
</template>

<script>

export default {
  name: 'HomePage',
}
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

.backgroundImage {
  background-image: url('/images/background-gold.png');
  background-size: contain;
  background-position: center;
  height: 100vh;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
.backgroundImageBlur {
  background-image: url('/images/background-gold.png');
  background-size: contain;
  background-position: center;
  height: 100vh;
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

  height: 26vh;
  width: 26vh;
  top: 60vh;
  left: calc(50vw - 25vh);

  @media (max-aspect-ratio: 1024/1792) {
    width:30vw;
    height:30vw;
    top: calc(50vh + 15vw);
    left: 18vw;
  }

}

.link-2 {
  position:absolute;

  border-radius: 50%;
  transition: background-color 1.0s ease;
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }

  height: 26vh;
  width: 26vh;
  top: 63vh;
  left: calc(50vw + 1vh);

  @media (max-aspect-ratio: 1024/1792) {
    width:30vw;
    height:30vw;
    top: calc(50vh + 20vw);
    left: 52vw;
  }
}


</style>
