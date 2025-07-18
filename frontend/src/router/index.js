import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/user',
      name: 'userHome',
      component: () => import('../views/user/UserHome.vue')
    },
    {
      path: '/admin',
      name: "adminHome",
      component: () => import('../views/admin/AdminHome.vue')
    },
    {
      path: '/admin/summary',
      name: 'adminSummary',
      component: () => import('../views/admin/Summary.vue')
    }
  ],
})

export default router
