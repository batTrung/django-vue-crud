/* eslint-disable */

export default {
  getAccess() {
    return window.localStorage.getItem('access_token')
  },

  getRefresh() {
    return window.localStorage.getItem('refresh_token')
  },

  saveToken({ access_token, refresh_token }) {
    window.localStorage.setItem('access_token', access_token)
    window.localStorage.setItem('refresh_token', refresh_token)
  },

  updateAccess(access_token) {
    window.localStorage.setItem('access_token', access_token)
  },

  destroyToken() {
    window.localStorage.removeItem('access_token')
    window.localStorage.removeItem('refresh_token')
  },
}
