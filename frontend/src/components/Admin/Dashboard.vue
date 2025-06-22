<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Users, ShoppingCart, DollarSign } from "lucide-vue-next";
import api from "@/api";

const totalUsers = ref(0);
const totalOrders = ref(0);
const totalRevenue = ref(0);

async function loadDashboardData() {
  try {
    const response = await api.get("/dashboard/");
    const data = response.data;
    totalUsers.value = data.totalUsers;
    totalOrders.value = data.totalOrders;
    totalRevenue.value = data.totalRevenue;
  } catch (error) {
    console.error("Erro ao carregar dados do dashboard:", error);
  }
}

onMounted(() => {
  loadDashboardData();
});

function formatCurrency(value: number) {
  return value.toLocaleString("pt-BR", {
    style: "currency",
    currency: "USD",
  });
}
</script>

<template>
  <div class="p-6 space-y-6 bg-gray-50 dark:bg-gray-900 min-h-screen">
    <h1 class="text-3xl font-semibold text-gray-800 dark:text-white">Dashboard</h1>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Usuários -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 flex items-center gap-4 transition hover:shadow-lg">
        <div class="bg-blue-100 dark:bg-blue-900 p-3 rounded-full">
          <Users class="w-6 h-6 text-blue-600 dark:text-blue-300" />
        </div>
        <div>
          <p class="text-sm text-gray-500 dark:text-gray-400">Total Users</p>
          <p class="text-2xl font-bold text-gray-800 dark:text-white">{{ totalUsers }}</p>
        </div>
      </div>

      <!-- Pedidos -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 flex items-center gap-4 transition hover:shadow-lg">
        <div class="bg-green-100 dark:bg-green-900 p-3 rounded-full">
          <ShoppingCart class="w-6 h-6 text-green-600 dark:text-green-300" />
        </div>
        <div>
          <p class="text-sm text-gray-500 dark:text-gray-400">Total Orders</p>
          <p class="text-2xl font-bold text-gray-800 dark:text-white">{{ totalOrders }}</p>
        </div>
      </div>

      <!-- Receita -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 flex items-center gap-4 transition hover:shadow-lg">
        <div class="bg-yellow-100 dark:bg-yellow-900 p-3 rounded-full">
          <DollarSign class="w-6 h-6 text-yellow-600 dark:text-yellow-300" />
        </div>
        <div>
          <p class="text-sm text-gray-500 dark:text-gray-400">Total Sold</p>
          <p class="text-2xl font-bold text-gray-800 dark:text-white">{{ formatCurrency(totalRevenue) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
