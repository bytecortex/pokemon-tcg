<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface User {
  id: number
  name: string
  email: string
  role: string
}

const users = ref<User[]>([])

// 🔁 Simulação de dados (substitua por API futuramente)
function loadUsers() {
  users.value = [
    { id: 1, name: 'Alice', email: 'alice@example.com', role: 'admin' },
    { id: 2, name: 'Bob', email: 'bob@example.com', role: 'user' },
    { id: 3, name: 'Charlie', email: 'charlie@example.com', role: 'user' }
  ]
}

onMounted(() => {
  loadUsers()
})
</script>

<template>
  <div class="p-6 space-y-6">
    <h1 class="text-2xl font-semibold text-gray-800 dark:text-white">User List</h1>

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
          <tr v-for="user in users" :key="user.id" class="border-b border-gray-200 dark:border-gray-700">
            <td class="p-2">{{ user.id }}</td>
            <td class="p-2">{{ user.name }}</td>
            <td class="p-2">{{ user.email }}</td>
            <td class="p-2 capitalize">{{ user.role }}</td>
          </tr>
          <tr v-if="users.length === 0">
            <td colspan="4" class="text-center py-4 text-gray-500 dark:text-gray-400">No users found.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
