<script setup lang="ts">
import router from "@/router";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { useRoute } from "vue-router";
import { ref, watch, onMounted } from "vue";
import { useUserStore } from "@/server/userStore";
import LoginDialog from "@/components/LoginDialog.vue";
import RegisterDialog from "@/components/RegisterDialog.vue";
import { Sun, Moon, ShoppingCart, Search } from "lucide-vue-next";

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

// Indexamento dos botões
type button = "Cards" | "Events" | "Cart" | "Home";

function handleClick(origin: button) {
  switch (origin) {
    case "Cards":
      router.push("/cards");
      break;
    case "Events":
      router.push("/events");
      break;
    case "Cart":
      router.push("/cart");
      break;
    case "Home":
      router.push("/");
      break;
    default:
      router.push("/");
  }
}

const route = useRoute();

function buttonClass(path: string) {
  if (route.path === path) {
    return [
      "h-8 flex rounded-xl items-center transition font-semibold text-primary text-white bg-blue-600",
    ];
  }
}

const searchQuery = ref("");

function performSearch() {
  const cleanedQuery = searchQuery.value.trim().replace(/\s+/g, " ");
  if (cleanedQuery !== "") {
    router.push({ path: "/cards", query: { name: cleanedQuery } });
  }
}

const userStore = useUserStore();
</script>

<template>
  <header
    class="grid grid-cols-3 items-center px-6 py-4 gap-x-4 bg-white dark:bg-black"
  >
    <!-- Logo -->
    <div class="text-2xl font-bold text-primary cursor-pointer select-none">
      <img
        :src="darkMode ? '/poqg-black-logo.png' : '/poqg-white-logo.png'"
        @click="handleClick('Home')"
        class="w-30"
      />
    </div>

    <!-- Busca -->
    <div class="relative max-w-md w-full mx-auto">
      <Input
        id="search"
        type="text"
        placeholder="Search..."
        class="pl-10 w-full"
        v-model="searchQuery"
        @keyup.enter="performSearch"
      />
      <span
        class="absolute left-0 inset-y-0 flex items-center justify-center px-2"
      >
        <Search class="size-4.5 text-muted-foreground" />
      </span>
    </div>

    <!-- Botões -->
    <div class="flex justify-end items-center space-x-4">
      <button
        @click="toggleDarkMode"
        aria-label="Toggle Dark Mode"
        class="cursor-pointer text-gray-600 dark:text-gray-300 hover:text-primary transition"
      >
        <component :is="darkMode ? Sun : Moon" class="w-6 h-6" />
      </button>

      <button
        aria-label="Cart"
        class="cursor-pointer relative text-gray-600 dark:text-gray-300 hover:text-primary transition"
        v-if="userStore.user"
      >
        <ShoppingCart class="w-6 h-6" />
        <span
          class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full text-xs w-5 h-5 flex items-center justify-center"
        >
          3
        </span>
      </button>

      <LoginDialog />
      <RegisterDialog />
    </div>
  </header>

  <div
    class="border-t border-b border-blue-600 flex justify-center space-x-25 h-10 py-0.75 bg-white dark:bg-black text-gray-800 dark:text-gray-300"
  >
    <Button
      @click="handleClick('Home')"
      :class="buttonClass('/')"
      class="h-8 flex rounded-xl items-center hover:text-primary transition font-semibold"
      variant="ghost"
    >
      Home
    </Button>
    <Button
      @click="handleClick('Cards')"
      :class="buttonClass('/cards')"
      class="h-8 flex rounded-xl items-center hover:text-primary transition font-semibold"
      variant="ghost"
    >
      Cards
    </Button>
    <Button
      @click="handleClick('Cart')"
      :class="buttonClass('/cart')"
      class="h-8 flex rounded-xl items-center hover:text-primary transition font-semibold"
      variant="ghost"
    >
      Cart
    </Button>
    <Button
      @click="handleClick('Events')"
      class="h-8 flex rounded-xl items-center hover:text-primary transition font-semibold"
      variant="ghost"
    >
      Events
    </Button>
  </div>
</template>
