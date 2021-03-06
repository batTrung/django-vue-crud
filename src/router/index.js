import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home'),
    },
    {
      path: '/books',
      name: 'book-list',
      component: () => import('@/views/BookList'),
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('@/views/Contact'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/About'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/Login'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/Register'),
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('@/views/Settings'),
      meta: {
        isRequiresAuth: true,
      },
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: () => import('@/views/Profile'),
      meta: {
        isRequiresAuth: true,
      },
    },
    {
      path: '*',
      name: '404',
      component: () => import('@/views/404'),
    },
  ]
})
