import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/pages/Dashboard.vue'),
  },
  {
    path: '/managebooks',
    component: () => import('@/pages/ManageBooks.vue'),
    name: 'ManageBooks',
  },
  {
    path: '/addbook',
    component: () => import('@/pages/AddBooks.vue'),
    name: 'AddBook',
  },
  {
    path: '/members',
    component: () => import('@/pages/Members.vue'),
    name: 'Members',
  },

]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
