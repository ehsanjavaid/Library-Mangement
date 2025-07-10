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

]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
