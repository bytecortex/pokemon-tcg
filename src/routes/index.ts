import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/HomePage.vue'
import CardsPage from '@/pages/CardsPage.vue'
import EventsPage from '@/pages/EventsPage.vue'
import CartPage from '@/pages/CartPage.vue'

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
  },
  {
    path: '/events',
    name: 'Events',
    component: EventsPage
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
