<template>
  <div class="row h-100 justify-content-center">
    <div class="col-lg-6 col-md-8 col-sm-10 my-4">
      <div class="card bg-light">
        <div class="card-body">
          <h1 class="card-title text-center">Đăng nhập</h1>
          <form method="post" v-on:submit.prevent="onSubmit()">
            <VErrors :errors="errors" v-if="errors" />
            <div class="form-group">
              <label for="id_email">Email</label>
              <input type="text" v-model.trim="user.email" class="form-control" :class="{'is-invalid': submitted && $v.user.email.$invalid }" id="id_email">
              <p class="invalid-feedback">
                <ul class="list-unstyled">
                  <li v-if="!$v.user.email.required">Trường này là bắt buộc</li>
                  <li v-if="!$v.user.email.email">Địa chỉ email không hợp lệ</li>
                </ul>
              </p>
            </div>
            <div class="form-group">
              <label for="id_password">Mật khẩu</label>
              <input type="password" v-model.trim="user.password" class="form-control" :class="{'is-invalid': submitted && $v.user.password.$invalid }" id="id_password">
              <p class="invalid-feedback">
                <ul class="list-unstyled">
                  <li v-if="!$v.user.password.required">Trường này là bắt buộc</li>
                </ul>
              </p>
            </div>
            <button type="submit" class="btn btn-block btn-success">Đăng nhập</button>
          </form>
          <div class="d-flex justify-content-between my-4">
            <div>
              Nếu chưa có tài khoản hãy
              <router-link :to="{name: 'register'}">
                Đăng ký
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex'
import { required, email } from 'vuelidate/lib/validators'
import VErrors from '@/components/VErrors'

import {
  LOGIN,
} from '@/store/actions.type.js'

export default {
  name: 'Login',
  title: 'Đăng nhập',
  components: {
    VErrors,
  },
  data() {
    return {
      user: {
        email: null,
        password: null,
      },
      submitted: false,
    }
  },
  validations: {
    user: {
      email: {
        required,
        email,
      },
      password: {
        required,
      },
    },
  },
  computed: {
    ...mapState({
      errors: state => state.auth.errors
    })
  },
  methods: {
    onSubmit() {
      this.submitted = true
      this.$store.dispatch(LOGIN, this.user)
        .then(() => this.$router.push(
          this.$route.query.redirect || { name: 'home' }))
    },
  },
}
</script>
