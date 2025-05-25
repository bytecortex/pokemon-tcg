import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import CardsPage from '@/pages/CardsPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cards',
    name: 'Cards',
    component: CardsPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
