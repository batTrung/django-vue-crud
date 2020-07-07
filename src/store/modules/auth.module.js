import JwtService from '@/common/jwt.service'
import ApiService from '@/common/api.service'
import {
  LOGIN,
  REGISTER,
  LOGOUT,
  CHECK_AUTH,
} from '@/store/actions.type.js'
import {
  SET_ERROR,
  SET_AUTH,
  PURGE_AUTH,
} from '@/store/mutations.type.js'

const state = {
  errors: null,
  user: {},
  isAuthenticated: false,
}

const getters = {
  currentUser(state) {
    return state.user
  },
  isAuthenticated(state) {
    return state.isAuthenticated
  },
}

const actions = {
  [LOGIN](context, credentials) {
    return new Promise((resolve, reject) => {
      ApiService.post('rest-auth/login', credentials)
        .then(({ data }) => {
          context.commit(SET_AUTH, data)
          JwtService.saveToken(data)
          resolve(data)
        })
        .catch(({ response }) => {
          context.commit(
            SET_ERROR,
            ['Thông tin tài khoản đăng nhập không hợp lệ.'],
          )
          reject(response)
        })
    })
  },
  [LOGOUT](context) {
    context.commit(PURGE_AUTH)
  },
  [REGISTER](context, credentials) {
    return new Promise((resolve, reject) => {
      ApiService.post('rest-auth/registration', credentials)
        .then(({ data }) => {
          context.commit(SET_AUTH, data)
          JwtService.saveToken(data)
          resolve(data)
        })
        .catch(({ response }) => {
          context.commit(
            SET_ERROR,
            ['Thông tin tài khoản đăng ký không hợp lệ.'],
          )
          reject(response)
        })
    })
  },
  [CHECK_AUTH](context) {
    if (JwtService.getAccess()) {
      ApiService.setHeader()
      ApiService.get('rest-auth/user')
        .then(({ data }) => {
          context.commit(SET_AUTH, { user: data })
        })
        .catch(() => {
          context.commit(PURGE_AUTH)
        })
    } else {
      context.commit(PURGE_AUTH)
    }
  },
}

const mutations = {
  [SET_ERROR](state, error) {
    state.errors = error
  },
  [SET_AUTH](state, payload) {
    state.errors = null
    state.user = payload.user
    state.isAuthenticated = true
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false
    state.user = {}
    state.errors = null
    JwtService.destroyToken()
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
