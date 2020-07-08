import Vue from 'vue'
import Vuelidate from 'vuelidate'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

import App from './App.vue'
import router from '@/router'
import store from '@/store'
import { CHECK_AUTH } from '@/store/actions.type'
import * as filters from '@/common/filters'
import { titleMixin } from '@/common/mixins'

import ApiService from '@/common/api.service'
import JwtService from '@/common/jwt.service'

[
  Vuelidate,
  BootstrapVue,
].forEach((x) => Vue.use(x))

Vue.mixin(titleMixin)

Vue.config.productionTip = false

ApiService.init()

// register global utility filters.
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

router.beforeEach((to, from, next) => {
  const toLogin = !JwtService.getAccess() && to.matched.some(record => record.meta.isRequiresAuth)
  if (toLogin) {
    next({
      name: 'login',
      query: { redirect: to.fullPath }
    })
  } else {
    return Promise.all([store.dispatch(CHECK_AUTH)]).then(next)
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
