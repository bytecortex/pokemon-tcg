<script setup lang="ts">
import { ref } from 'vue'
import api from '@/api'

const cardId = ref('')
const card = ref<any>(null)
const loading = ref(false)
const error = ref<string | null>(null)

async function fetchCardById() {
  loading.value = true
  error.value = null
  try {
    const response = await api.get(`/cards/${cardId.value}`)
    card.value = response.data
  } catch (err) {
    console.error('Erro ao buscar carta:', err)
    error.value = 'Carta não encontrada.'
    card.value = null
  } finally {
    loading.value = false
  }
}

async function updateCard() {
  if (!card.value) return
  try {
    await api.put(`/cards/${card.value.id}`, {
      stock: card.value.stock,
      price: card.value.price,
    })
    alert('Carta atualizada com sucesso!')
  } catch (err) {
    console.error('Erro ao atualizar carta:', err)
    alert('Erro ao atualizar a carta.')
  }
}
</script>

<template>
  <div class="p-6 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-6">Manage Card</h1>

    <!-- Search card by ID -->
    <div class="mb-4 flex items-center space-x-2">
      <input v-model="cardId" type="text" placeholder="Enter card ID" class="border px-3 py-2 rounded w-full" />
      <button @click="fetchCardById" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        Search
      </button>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="text-gray-500">Searching for card...</div>

    <!-- Error -->
    <div v-if="error" class="text-red-600 mb-4">{{ error }}</div>

    <!-- Card edit form -->
    <div v-if="card" class="space-y-4 border-t pt-6 mt-6">
      <div>
        <label class="block text-sm font-medium text-gray-700">Name</label>
        <p class="font-semibold">{{ card.name }}</p>
      </div>

      <!-- Card Image -->
      <div v-if="card.images?.small" class="mt-2">
        <img :src="card.images.small" :alt="card.name" class="max-w-xs rounded shadow" />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700">Stock</label>
        <input type="number" v-model.number="card.stock" class="border px-3 py-2 rounded w-full" />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700">Price</label>
        <input type="number" step="0.01" v-model.number="card.price" class="border px-3 py-2 rounded w-full" />
      </div>

      <button @click="updateCard" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition">
        Save Changes
      </button>
    </div>
  </div>
</template>
