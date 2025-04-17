 <template>
   <UApp>
    <NuxtPage />
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

.page-enter-active,
.page-leave-active,
.page-enter-from {
  opacity: 0;
  transform: translate(50px, 0);
}
.page-leave-to {
  opacity: 0;
  transform: translate(-50px, 0);
}
</style>
