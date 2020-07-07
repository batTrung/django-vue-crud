import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import JwtService from '@/common/jwt.service'

const ApiService = {
  init() {
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = process.env.API_URL
    Vue.axios.defaults.xsrfCookieName = 'csrftoken'
    Vue.axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
  },

  setHeader() {
    Vue.axios.defaults.headers.common['Authorization'] = `Bearer ${JwtService.getAccess()}`
  },

  query(resource, params) {
    return Vue.axios.get(`${resource}/`, params).catch(error => {
      throw new Error(`[RWV] ApiService ${error}`)
    })
  },

  get(resource, slug = '') {
    return Vue.axios.get(`${resource}/${slug}`).catch(error => {
      throw new Error(`[RWV] ApiService ${error}`)
    })
  },

  post(resource, params) {
    return Vue.axios.post(`${resource}/`, params)
  },

  update(resource, slug, params) {
    return Vue.axios.put(`${resource}/${slug}/`, params)
  },

  put(resource, params) {
    return Vue.axios.put(`${resource}/`, params)
  },

  delete(resource) {
    return Vue.axios.delete(`${resource}/`).catch(error => {
      throw new Error(`[RWV] ApiService ${error}`)
    })
  },
}

export default ApiService

export const BooksService = {
  query(params) {
    return ApiService.query('books', {
      params: params
    })
  },
  create(params) {
    return ApiService.post('books', params)
  },
  destroy(slug) {
    return ApiService.delete(`books/${slug}`)
  },
  update(slug, params) {
    return ApiService.update('books', slug, params)
  },
  get(slug) {
    return ApiService.get('books', slug)
  },
}
