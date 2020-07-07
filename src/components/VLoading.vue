<template>
  <div class="text-center my-5" v-show="isLoading">
    <div class="spinner-grow text-success" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <div class="spinner-grow text-danger" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <div class="spinner-grow text-warning" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Loading',
  props: {
    isLoading: Boolean,
  },
}

</script>
