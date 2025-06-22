<script setup lang="ts">
import { ref } from 'vue';

const cardId = ref('');
const card = ref<any>(null);
const loading = ref(false);

function fetchCardById() {
  loading.value = true;

  // TODO: Implement API call
  setTimeout(() => {
    // Simulated card response
    card.value = {
      id: cardId.value,
      name: 'Sample Card',
      stock: 10,
      price: 19.99,
    };
    loading.value = false;
  }, 500);
}

function updateCard() {
  // TODO: Implement update API call
  alert(`Updating card ID ${card.value.id}`);
}
</script>

<template>
  <div class="p-6 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-6">Manage Card</h1>

    <!-- Search card by ID -->
    <div class="mb-4 flex items-center space-x-2">
      <input
        v-model="cardId"
        type="text"
        placeholder="Enter card ID"
        class="border px-3 py-2 rounded w-full"
      />
      <button
        @click="fetchCardById"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Search
      </button>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="text-gray-500">Searching for card...</div>

    <!-- Card edit form -->
    <div v-if="card" class="space-y-4 border-t pt-6 mt-6">
      <div>
        <label class="block text-sm font-medium text-gray-700">Name</label>
        <p class="font-semibold">{{ card.name }}</p>
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700">Stock</label>
        <input
          type="number"
          v-model.number="card.stock"
          class="border px-3 py-2 rounded w-full"
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700">Price</label>
        <input
          type="number"
          v-model.number="card.price"
          class="border px-3 py-2 rounded w-full"
        />
      </div>

      <button
        @click="updateCard"
        class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
      >
        Save Changes
      </button>
    </div>
  </div>
</template>
