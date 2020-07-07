<template>
  <div>
    <b-alert :variant="tag" show dismissible fade>
      {{ message }}
    </b-alert>
    <br>
  </div>
</template>
<script>
export default {
  props: {
    message: String,
    tag: {
      required: false,
      type: String,
      default: 'success',
    },
  },
}
</script>
