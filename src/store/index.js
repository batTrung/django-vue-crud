import Vue from 'vue'
import Vuex from 'vuex'

import book from './modules/book.module'
import auth from './modules/auth.module'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    book,
    auth,
  },
})
