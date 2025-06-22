<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'
import type { UserWithOrders } from '@/interfaces/user'

const search = ref('')
const loading = ref(false)
const error = ref<string | null>(null)
const usersWithOrders = ref<UserWithOrders[]>([])

async function fetchUsersOrders() {
    loading.value = true
    error.value = null

    try {
        const response = await api.get('/users-orders', {
            params: { name: search.value }
        })
        usersWithOrders.value = response.data
    } catch (err: any) {
        error.value = 'Erro ao buscar usuários com pedidos.'
    } finally {
        loading.value = false
    }
}

onMounted(() => {
    fetchUsersOrders()
})
</script>

<template>
    <div class="p-6 space-y-6">
        <h1 class="text-2xl font-semibold text-gray-800 dark:text-white">Pedidos por Usuário</h1>

        <div class="flex items-center space-x-4">
            <input v-model="search" @keyup.enter="fetchUsersOrders" placeholder="Buscar por nome..."
                class="px-4 py-2 border rounded w-64 dark:bg-gray-900 dark:text-white" />
            <button @click="fetchUsersOrders" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded shadow">
                Search
            </button>
        </div>

        <div v-if="error" class="text-red-600 dark:text-red-400">
            {{ error }}
        </div>

        <div class="bg-white dark:bg-gray-800 p-4 rounded shadow">
            <table class="w-full text-sm table-auto">
                <thead class="text-left text-gray-500 dark:text-gray-300 border-b dark:border-gray-700">
                    <tr>
                        <th class="p-2">ID</th>
                        <th class="p-2">Nome</th>
                        <th class="p-2">Email</th>
                        <th class="p-2">Total Orders</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="loading">
                        <td colspan="4" class="text-center py-4">Carregando...</td>
                    </tr>
                    <tr v-else-if="usersWithOrders.length === 0">
                        <td colspan="4" class="text-center py-4">Nenhum resultado encontrado.</td>
                    </tr>
                    <tr v-for="user in usersWithOrders" :key="user.id"
                        class="border-b border-gray-200 dark:border-gray-700">
                        <td class="p-2">{{ user.id }}</td>
                        <td class="p-2">{{ user.name }}</td>
                        <td class="p-2">{{ user.email }}</td>
                        <td class="p-2">{{ user.total_orders }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

