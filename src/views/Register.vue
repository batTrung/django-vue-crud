<template>
  <div class="row h-100 justify-content-center">
    <div class="col-lg-6 col-md-8 col-sm-10 my-4">
      <div class="card bg-light">
        <div class="card-body">
          <h1 class="card-title text-center">Đăng ký</h1>
          <form method="post" @submit.prevent="onSubmit()">
            <VErrors :errors="errors" v-if="errors" />
            <div class="form-group">
              <label for="id_email">Email</label>
              <input type="text" v-model.trim="$v.user.email.$model" class="form-control" @keyup="checkEmailExists($event.target.value)" id="id_email">
              <ul class="list-unstyled text-danger" v-show="$v.user.email.$anyDirty">
                <li v-if="!$v.user.email.required">Trường này là bắt buộc</li>
                <li v-if="!$v.user.email.email">Địa chỉ email không hợp lệ</li>
                <li v-if="emailExists">Địa chỉ email đã được sử dụng. Vui lòng chọn email khác.</li>
                <li v-if="!$v.user.email.maxLength">Email quá dài, chỉ tối đa là {{ $v.user.email.$params.maxLength.max }} từ </li>
              </ul>
            </div>
            <div class="form-group">
              <label for="id_password">Mật khẩu</label>
              <input type="password" v-model.trim="$v.user.password1.$model" class="form-control" id="id_password1">
              <ul class="list-unstyled text-danger" v-show="$v.user.password1.$anyDirty">
                <li v-if="!$v.user.password1.required">Trường này là bắt buộc</li>
                <li v-if="!$v.user.password1.minLength">Mật khẩu quá ngắn, tối thiểu là {{ $v.user.password1.$params.minLength.min }} từ </li>
                <li v-if="!$v.user.password1.maxLength">Mật khẩu quá dài, chỉ tối đa là {{ $v.user.password1.$params.maxLength.max }} từ </li>
              </ul>
            </div>
            <div class="form-group">
              <label for="id_password">Nhập lại mật khẩu</label>
              <input type="password" v-model.trim="$v.user.password2.$model" class="form-control" id="id_password2">
              <ul class="list-unstyled text-danger" v-show="$v.user.password2.$anyDirty">
                <li v-if="!$v.user.password2.required">Trường này là bắt buộc</li>
                <li v-if="!$v.user.password2.sameAsPassword1">Mật khẩu không khớp</li>
                <li v-if="!$v.user.password2.minLength">Mật khẩu quá ngắn, tối thiểu là {{ $v.user.password2.$params.minLength.min }} từ </li>
                <li v-if="!$v.user.password2.maxLength">Mật khẩu quá dài, chỉ tối đa là {{ $v.user.password2.$params.maxLength.max }} từ </li>
              </ul>
            </div>
            <button type="submit" class="btn btn-block btn-success" :disabled="$v.user.$invalid || emailExists">
              Đăng ký
            </button>
          </form>
          <div class="d-flex justify-content-between my-4">
            <div>
              Nếu đã có tài khoản hãy
              <router-link :to="{name: 'login'}">
                Đăng nhập
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
import ApiService from '@/common/api.service'
import {
  REGISTER,
} from '@/store/actions.type.js'
import VErrors from '@/components/VErrors'
import { required, minLength, maxLength, email, sameAs } from 'vuelidate/lib/validators'

export default {
  name: 'Register',
  title: 'Đăng ký',
  components: {
    VErrors,
  },
  data() {
    return {
      emailExists: false,
      user: {
        email: '',
        password1: '',
        password2: '',
      },
    }
  },
  validations: {
    user: {
      email: {
        required,
        email,
        maxLength: maxLength(250),
      },
      password1: {
        required,
        minLength: minLength(8),
        maxLength: maxLength(250),
      },
      password2: {
        required,
        minLength: minLength(8),
        maxLength: maxLength(250),
        sameAsPassword1: sameAs('password1'),
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
      const valid = !this.$v.user.$anyError && !this.emailExists
      if (valid) {
        this.$store.dispatch(REGISTER, this.user)
          .then(() => this.$router.push(
            this.$route.query.redirect || { name: 'home' }
          ))
      }
    },
    checkEmailExists(email) {
      ApiService.get('account/check-email-exists', email)
        .then(({ data }) => {
          this.emailExists = data.invalid
        })
    },
  },
}
</script>
