import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/login/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/home/Home.vue'),
  },

  
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
