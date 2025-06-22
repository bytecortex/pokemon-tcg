<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { LayoutDashboard, Users, Settings, Sun, Moon } from "lucide-vue-next";
import { useUserStore } from "@/server/userStore";

const router = useRouter();
const route = useRoute();
const userStore = useUserStore();

const darkMode = ref(false);

// Dark mode igual ao header
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

function isActive(path: string) {
  return route.path === path
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
      <img
        :src="darkMode ? '/poqg-black-logo.png' : '/poqg-white-logo.png'"
        alt="Logo"
        class="w-32 mx-auto cursor-pointer"
        @click="navigate('/')"
      />
    </div>

    <!-- Main Navigation -->
    <nav class="flex flex-col space-y-2">
      <span class="text-xs text-gray-500 uppercase px-4 tracking-wider">ADMIN PANEL</span>

      <button
        class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
               border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive('/admin/dashboard')"
        @click="navigate('/admin/dashboard')"
      >
        <LayoutDashboard class="w-5 h-5" />
        <span>Dashboard</span>
      </button>

      <button
        class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
               border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive('/admin/users')"
        @click="navigate('/admin/users')"
      >
        <Users class="w-5 h-5" />
        <span>Users</span>
      </button>

      <button
        class="flex items-center space-x-3 px-4 py-2 rounded transition font-medium cursor-pointer
               border border-transparent hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-gray-800"
        :class="isActive('/admin/settings')"
        @click="navigate('/admin/settings')"
      >
        <Settings class="w-5 h-5" />
        <span>Settings</span>
      </button>
    </nav>

    <!-- Separator -->
    <div class="my-4 border-t border-gray-300 dark:border-gray-700"></div>

    <!-- Preferences & Theme -->
    <div class="px-4">
      <span class="text-xs text-gray-500 uppercase tracking-wider">Preferences</span>

      <button
        @click="toggleDarkMode"
        class="mt-2 flex items-center space-x-2 text-gray-600 dark:text-gray-300 hover:text-primary transition cursor-pointer"
        aria-label="Toggle Dark Mode"
      >
        <component :is="darkMode ? Sun : Moon" class="w-5 h-5" />
        <span class="text-sm">
          {{ darkMode ? 'Dark Mode' : 'Light Mode' }}
        </span>
      </button>
    </div>

    <!-- Logout -->
    <div class="mt-auto pt-6 px-4">
      <div class="border-t border-gray-300 dark:border-gray-700 pt-4">
        <button
          class="w-full flex items-center space-x-3 text-left text-sm text-red-500 hover:text-red-600 hover:bg-red-100 dark:hover:bg-red-900 
                 rounded px-3 py-2 font-medium cursor-pointer transition border border-transparent hover:border-red-300"
          @click="userStore.logout()"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1m0-10V5" />
          </svg>
          <span>Log Out</span>
        </button>
      </div>
    </div>
  </aside>
</template>


