<script setup lang="ts">
import AdminAside from "@/components/Admin/AsideNav.vue";
import AdminDashboard from "@/components/Admin/Dashboard.vue";
</script>

<template>
  <div class="flex h-screen overflow-hidden">
    <nav class="w-64 flex-shrink-0 h-full">
      <AdminAside />
    </nav>
    <main class="flex-grow h-full overflow-y-auto bg-gray-50 dark:bg-gray-900">
      <AdminDashboard />
    </main>
  </div>
</template>