<script setup lang="ts">
import { ref, onMounted } from 'vue';
import api from '@/api';
import type { Order } from '@/interfaces/order';
import { Skeleton } from '@/components/ui/skeleton';
import OrderCard from '@/components/OrderCard.vue';

const orders = ref<Order[]>([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const { data } = await api.get('/orders/history');
    orders.value = data;
  } catch (error) {
    console.error('Erro ao carregar histórico de pedidos:', error);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h1 class="text-2xl font-semibold mb-6">Histórico de Pedidos</h1>

    <div v-if="loading" class="space-y-4">
      <Skeleton class="h-20 w-full rounded-md" v-for="n in 3" :key="n" />
    </div>

    <div v-else-if="orders.length === 0" class="ay-500"text-gr>
      Nenhum pedido encontrado.
    </div>

    <div v-else class="space-y-4">
      <OrderCard v-for="order in orders" :key="order.id" :order="order" />
    </div>
  </div>
</template>
