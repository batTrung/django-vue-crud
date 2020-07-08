<template>
  <div>
    <div class="text-center pt-5">
      <h1 class="display-4">(404) Page Not Found!</h1>
      <p>
        <router-link :to="{ name: 'home' }" class="btn btn-success my-2 mr-2" role="button">
          Trang chủ
        </router-link>
        <router-link :to="{ name: 'book-list' }" class="btn btn-primary my-2" role="button">
          <i class="fa fa-code"></i> DEMO
        </router-link>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: '404',
}
</script>
