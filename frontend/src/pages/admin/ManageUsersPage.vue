<script setup lang="ts">
import AdminAside from "@/components/Admin/AsideNav.vue";
import AdminManageUsers from "@/components/Admin/ManageUsers.vue";
</script>

<template>
  <div class="flex min-h-screen">
    <AdminAside />
    <main class="flex-grow p-6 bg-gray-50 dark:bg-gray-900">
      <AdminManageUsers />
    </main>
  </div>
</template>