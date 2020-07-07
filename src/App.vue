<template>
  <div id="app">
    <TheHeader />
    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>
<script>
import TheHeader from '@/components/TheHeader'

export default {
  name: 'App',
  components: {
    TheHeader,
  },
}
</script>
<style>
.modal-backdrop {
  opacity: 0.7;
}

/*.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.modal {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    display: block;
    overflow: hidden;
    transition: opacity .3s ease;
}*/

</style>
