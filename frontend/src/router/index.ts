import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/HomePage.vue'
import CardsPage from '@/pages/CardsPage.vue'
import OrdersPage from '@/pages/OrdersPage.vue'
import CartPage from '@/pages/CartPage.vue'
import AdminPage from '@/pages/admin/DashboardPage.vue'
import ManageCardsPage from '@/pages/admin/ManageCardsPage.vue'
import ManageUsersPage from '@/pages/admin/ManageUsersPage.vue'
import UsersOrdersPage from '@/pages/admin/UsersOrdersPage.vue'
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
    path: '/orders',
    name: 'Orders',
    component: OrdersPage
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartPage
  },
  {
    path: "/admin",
    component: AdminPage,
    meta: { requiresAdmin: true },
  },
  {
    path: "/admin/cards",
    component: ManageCardsPage,
    meta: { requiresAdmin: true },
  },
  {
    path: "/admin/users",
    component: ManageUsersPage,
    meta: { requiresAdmin: true },
  },
    {
    path: "/admin/usersOrders",
    component: UsersOrdersPage,
    meta: { requiresAdmin: true },
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Verifica se o usuário é admin quando a rota requer acesso de admin
router.beforeEach((to, _from, next) => {
  const userStore = useUserStore();

  if (to.meta.requiresAdmin && userStore.user?.role !== 'admin') {
    alert("Acesso negado: painel administrativo apenas para admins");
    next('/');
  } else {
    next();
  }
});

export default router
