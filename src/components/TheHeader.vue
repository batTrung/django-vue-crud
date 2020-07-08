<template>
  <b-navbar toggleable="lg" type="dark" style="background-color: #758AA2">
    <div class="container">
      <b-navbar-brand :to="{name: 'home'}">DjangoVue</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{name: 'book-list'}">Books</b-nav-item>
          <b-nav-item :to="{name: 'about'}">About</b-nav-item>
          <b-nav-item :to="{name: 'contact'}">Contact</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form v-if="!isAuthenticated">
            <router-link :to="{name: 'login'}" class="btn btn-success mr-2">
              Đăng nhập
            </router-link>
            <router-link :to="{name: 'register'}" class="btn btn-primary mr-2">
              Đăng ký
            </router-link>
          </b-nav-form>
          <b-nav-item-dropdown :text="currentUser.username" right v-else>
            <b-dropdown-item :to="{name: 'profile', params: {username: currentUser.username}}">Trang cá nhân</b-dropdown-item>
            <b-dropdown-item :to="{name: 'settings'}">Cài đặt</b-dropdown-item>
            <div class="dropdown-divider"></div>
            <b-dropdown-item @click="logout">Đăng xuất</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </div>
  </b-navbar>
</template>
<script>
import { LOGOUT } from '@/store/actions.type'
import { mapGetters } from 'vuex'

export default {
  name: 'TheHeader',
  computed: {
    ...mapGetters(['currentUser', 'isAuthenticated'])
  },
  methods: {
    logout() {
      this.$store.dispatch(LOGOUT).then(() => {
        this.$router.push({ name: 'home' })
          .catch(() => {})
      })
    }
  },
}
</script>
