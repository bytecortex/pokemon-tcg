<script setup lang="ts">
import { ref, onMounted } from 'vue';
import api from '@/api';
import type { Order } from '@/interfaces/order';
import OrderCard from '@/components/OrderCard.vue';
import OrderDialog from '@/components/OrderDialog.vue';
import { Skeleton } from '@/components/ui/skeleton';

const orders = ref<Order[]>([]);
const loading = ref(true);
const selectedOrderId = ref<number | null>(null);

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

    <div v-else-if="orders.length === 0" class="text-gray-500">
      Nenhum pedido encontrado.
    </div>

    <div v-else class="space-y-4">
      <button
        v-for="order in orders"
        :key="order.id"
        @click="selectedOrderId = order.id"
        class="block w-full text-left cursor-pointer transition-shadow duration-300 hover:shadow-[0_0_10px_2px_rgba(59,130,246,0.7)]"
      >
        <OrderCard :order="order" />
      </button>
    </div>

    <OrderDialog 
      v-if="selectedOrderId !== null" 
      :orderId="selectedOrderId" 
      :open="selectedOrderId !== null" 
      @close="selectedOrderId = null" 
    />
  </div>
</template>
