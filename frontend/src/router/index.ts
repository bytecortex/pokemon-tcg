import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/HomePage.vue'
import CardsPage from '@/pages/CardsPage.vue'
import EventsPage from '@/pages/EventsPage.vue'
import CartPage from '@/pages/CartPage.vue'
import { useUserStore } from '@/server/userStore';

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
  },
  {
    path: "/admin",
    component: () => import('@/pages/admin/AdminPanel.vue'),
    meta: { requiresAdmin: true },
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Verifica se o usuário é admin quando a rota requer acesso de admin
router.beforeEach((to, from, next) => {
  const userStore = useUserStore();

  if (to.meta.requiresAdmin && userStore.user?.role !== 'admin') {
    alert("Acesso negado: painel administrativo apenas para admins");
    next('/');
  } else {
    next();
  }
});

export default router
