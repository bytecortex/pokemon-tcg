<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'

interface Card {
  card_id: number
  card_name: string
  total_sold: number
  price: number
  total_sales: number
}

const cards = ref<Card[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

async function fetchTopSellingCards() {
  loading.value = true
  error.value = null

  try {
    const response = await api.get('/admin/top-selling-cards')
    cards.value = response.data
  } catch (err: any) {
    console.error('Error loading top-selling cards:', err)
    error.value = 'Error loading top-selling cards.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchTopSellingCards()
})

// Function to format values as currency
const currency = (value: number): string => {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  }).format(value)
}
</script>

<template>
  <div class="p-6 space-y-6">
    <h1 class="text-2xl font-semibold text-gray-800 dark:text-white">Top Selling Cards</h1>

    <!-- Error -->
    <div v-if="error" class="text-red-600 dark:text-red-400">
      {{ error }}
    </div>

    <!-- Cards Table -->
    <div v-if="loading" class="text-gray-500 dark:text-gray-400">
      Loading top-selling cards...
    </div>

    <div v-else>
      <div class="bg-white dark:bg-gray-800 p-4 rounded shadow">
        <table class="w-full text-sm table-auto">
          <thead class="text-left text-gray-500 dark:text-gray-300 border-b dark:border-gray-700">
            <tr>
              <th class="p-2">ID</th>
              <th class="p-2">Name</th>
              <th class="p-2">Total Sold</th>
              <th class="p-2">Total Sales</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="cards.length === 0">
              <td colspan="5" class="text-center py-4 text-gray-500 dark:text-gray-400">No cards found.</td>
            </tr>
            <tr v-for="card in cards" :key="card.card_id" class="border-b border-gray-200 dark:border-gray-700">
              <td class="p-2">{{ card.card_id }}</td>
              <td class="p-2">{{ card.card_name }}</td>
              <td class="p-2">{{ card.total_sold }}</td>
              <td class="p-2">{{ currency(card.total_sales) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
