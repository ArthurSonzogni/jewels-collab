 <template>
   <UApp>
    <Navbar />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </UApp>
</template>

<style lang="scss">

body {
  box-sizing: border-box;
  font-family: "Playfair", sans-serif;
  margin: 0;
  padding: 0;
}

.font-title {
  font-family: "Cinzel", sans-serif;
} 

.page-enter-active {
  transition: all 0.3s;
}

.page-leave-active {
  transition: all 0.3s;
}

.page-enter-from {
  opacity: 0;
  transform: translate(50px, 0);
}

.page-leave-to {
  opacity: 0;
  transform: translate(-50px, 0);
}
</style>
