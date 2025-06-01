import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },

  {
    path: '/members',
    name: 'members',
    component: () => import('@/pages/Member.vue'),
  },
  {
    path: '/members/:id',
    name: 'member',
    component: () => import('@/pages/MemberDetail.vue'),
  },
  {
    path: '/books',
    name: 'books',
    component: () => import('@/pages/book.vue'),
  },
]


let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
