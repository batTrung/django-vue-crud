<template>
  <div>
    <div class="alert alert-block alert-danger" v-if="errors">
      <ul class="m-0">
        <li v-for="(error, index) in errors" :key="index">
          {{ error }}
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Errors',
  props: {
    errors: Array,
  },
}

</script>
