<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { LayoutDashboard, Users, Sun, Moon } from "lucide-vue-next";
import { useUserStore } from "@/server/userStore";

const router = useRouter();
const route = useRoute();
const userStore = useUserStore();

const darkMode = ref(false);

function toggleDarkMode() {
  darkMode.value = !darkMode.value;
}

onMounted(() => {
  const savedMode = localStorage.getItem("darkMode");
  if (savedMode === "true" || savedMode === "false") {
    darkMode.value = savedMode === "true";
  } else {
    darkMode.value = window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
});

watch(darkMode, (newVal) => {
  localStorage.setItem("darkMode", String(newVal));
  if (newVal) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }
});

function isActive(paths: string[]) {
  return paths.includes(route.path)
    ? "bg-blue-600 text-white"
    : "hover:bg-gray-100 dark:hover:bg-gray-800";
}

function navigate(path: string) {
  router.push(path);
}
</script>

<template>
  <aside class="h-screen w-64 bg-white dark:bg-black shadow-lg flex flex-col p-4">
    <!-- Logo -->
    <div class="mb-8 text-center">
      <img :src="darkMode ? '/poqg-black-logo.png' : '/poqg-white-logo.png'" alt="Logo"
        class="w-32 mx-auto cursor-pointer" @click="navigate('/admin')" />
    </div>

    <!-- Main Navigation -->
    <nav class="flex flex-col space-y-2">
      <span class="text-xs text-gray-500 uppercase px-4 tracking-wider">ADMIN PANEL</span>

      <button class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
               border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive(['/admin'])" @click="navigate('/admin')">
        <LayoutDashboard class="w-5 h-5" />
        <span>Dashboard</span>
      </button>

      <button class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
               border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive(['/admin/users', '/admin/usersOrders'])" @click="navigate('/admin/users')">
        <Users class="w-5 h-5" />
        <span>Users</span>
      </button>

      <button class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
   border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive(['/admin/cards'])" @click="navigate('/admin/cards')">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <rect x="3" y="2" width="18" height="20" rx="3" ry="3" stroke-width="2" stroke-linecap="round"
            stroke-linejoin="round" />
        </svg>
        <span>Cards</span>
      </button>

      <button class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
   border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive(['/admin/cardsTopSellers'])" @click="navigate('/admin/cardsTopSellers')">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M12 17.27l6.18 3.73-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73-1.64 7.03L12 17.27z" />
        </svg>
        <span>Top Selling Cards</span>
      </button>

      <!-- <button class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
               border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive('/admin/settings')" @click="navigate('/admin/')">
        <Settings class="w-5 h-5" />
        <span>Settings</span>
      </button> -->
    </nav>

    <!-- Separator -->
    <div class="my-4 border-t border-gray-300 dark:border-gray-700"></div>

    <!-- Preferences & Theme -->
    <div class="px-4">
      <span class="text-xs text-gray-500 uppercase tracking-wider">Preferences</span>

      <button @click="toggleDarkMode"
        class="mt-2 flex items-center space-x-2 text-gray-600 dark:text-gray-300 hover:text-primary transition cursor-pointer"
        aria-label="Toggle Dark Mode">
        <component :is="darkMode ? Sun : Moon" class="w-5 h-5" />
        <span class="text-sm">
          {{ darkMode ? 'Dark Mode' : 'Light Mode' }}
        </span>
      </button>
    </div>

    <!-- Logout e Home -->
    <div class="mt-auto pt-6 px-4">
      <div class="border-t border-gray-300 dark:border-gray-700 pt-4 flex flex-col space-y-4">

        <!-- Home -->
        <button class="flex items-center space-x-3 text-left text-sm text-gray-600 hover:text-gray-800 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-white dark:hover:bg-gray-800 
         rounded px-3 py-2 font-medium cursor-pointer transition border border-transparent hover:border-gray-300"
          @click="navigate('/')">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"
            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 9.75L12 3l9 6.75v10.5A2.25 2.25 0 0118.75 22.5H5.25A2.25 2.25 0 013 20.25V9.75z" />
            <path d="M9 22.5v-6h6v6" />
          </svg>
          <span>Home</span>
        </button>


        <!-- Logout -->
        <button class="flex items-center space-x-3 text-left text-sm text-red-500 hover:text-red-600 hover:bg-red-100 dark:hover:bg-red-900 
         rounded px-3 py-2 font-medium cursor-pointer transition border border-transparent hover:border-red-300"
          @click="userStore.logout()">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"
            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 17l5-5-5-5" />
            <path d="M21 12H9" />
            <path d="M9 19H5a2 2 0 01-2-2V7a2 2 0 012-2h4" />
          </svg>
          <span>Log Out</span>
        </button>

      </div>
    </div>
  </aside>
</template>
