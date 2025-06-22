<script setup lang="ts">
import type { Order } from '@/interfaces/order';
defineProps<{ order: Order }>();
</script>

<template>
  <div class="border rounded-md p-4 shadow-sm hover:shadow-md transition">
    <div class="flex justify-between items-center mb-2">
      <div class="font-medium text-lg">Pedido #{{ order.id }}</div>
      <div class="text-sm text-gray-500">{{ new Date(order.created_at).toLocaleDateString() }}</div>
    </div>
    <div>Total: R$ {{ order.total_price.toFixed(2) }}</div>
  </div>
</template>
  