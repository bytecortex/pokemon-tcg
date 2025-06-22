<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'
import type { User } from '@/interfaces/user'


const users = ref<User[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

async function loadUsers() {
  loading.value = true
  error.value = null

  try {
    const response = await api.get<User[]>('/users')
    users.value = response.data
  } catch (err: any) {
    console.error('Erro ao carregar usuários:', err)
    error.value = 'Erro ao carregar usuários.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadUsers()
})
</script>

<template>
  <div class="p-6 space-y-6">
    <h1 class="text-2xl font-semibold text-gray-800 dark:text-white">User List</h1>

    <!-- Ver Pedidos -->
    <router-link to="/admin/usersOrders"
      class="inline-block bg-blue-600 hover:bg-blue-700 text-white font-medium px-4 py-2 rounded shadow">
      Total Orders 
    </router-link>

    <div v-if="error" class="text-red-600 dark:text-red-400">
      {{ error }}
    </div>

    <div class="bg-white dark:bg-gray-800 p-4 rounded shadow">
      <table class="w-full text-sm table-auto">
        <thead class="text-left text-gray-500 dark:text-gray-300 border-b dark:border-gray-700">
          <tr>
            <th class="p-2">ID</th>
            <th class="p-2">Name</th>
            <th class="p-2">Email</th>
            <th class="p-2">Role</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="4" class="text-center py-4 text-gray-500 dark:text-gray-400">Carregando usuários...</td>
          </tr>
          <tr v-else-if="users.length === 0">
            <td colspan="4" class="text-center py-4 text-gray-500 dark:text-gray-400">Nenhum usuário encontrado.</td>
          </tr>
          <tr v-for="user in users" :key="user.id" class="border-b border-gray-200 dark:border-gray-700">
            <td class="p-2">{{ user.id }}</td>
            <td class="p-2">{{ user.name }}</td>
            <td class="p-2">{{ user.email }}</td>
            <td class="p-2 capitalize">{{ user.role }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
