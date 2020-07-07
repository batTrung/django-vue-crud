<template>
  <div>
    <div class="text-center pt-5">
      <h1 class="display-4">Trang chủ</h1>
      <p class="lead text-muted">Ví dụ sử dụng <code>Django Rest Framework</code> với <code>Vuejs</code></p>
      <p>
        <a href="http://djangobat.com/" class="btn btn-success my-2 mr-2">djangobat.com</a>
        <router-link :to="{ name: 'book-list' }" class="btn btn-primary my-2" role="button">
          <i class="fa fa-code"></i> DEMO
        </router-link>
      </p>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Home',
  title: 'Trang chủ',
}
</script>
