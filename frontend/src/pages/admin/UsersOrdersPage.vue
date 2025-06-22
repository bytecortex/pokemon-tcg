<script setup lang="ts">
import AdminAside from "@/components/Admin/AsideNav.vue";
import UsersOrders from "@/components/Admin/UsersOrders.vue";
</script>

<template>
  <div class="flex min-h-screen">
    <AdminAside />
    <main class="flex-grow p-6 bg-gray-50 dark:bg-gray-900">
      <UsersOrders />
    </main>
  </div>
</template>