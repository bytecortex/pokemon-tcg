<script setup lang="ts">
import { ref } from "vue";
import { Sun, Moon, ShoppingCart, Search} from "lucide-vue-next"; 
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import Button from "./ui/button/Button.vue";
import Input from "./ui/input/Input.vue";

const darkMode = ref(false);
let mode = 'light';

function toggleDarkMode() {
  darkMode.value = !darkMode.value;
  if (darkMode.value) {
    document.documentElement.classList.add("dark");
    mode = 'dark';
  } else {
    document.documentElement.classList.remove("dark");
    mode = 'light';
  }
}

//todo: 
</script>

<template>
  <header class="flex items-center justify-between px-6 py-4 bg-white dark:bg-black shadow-md">
    <!-- Logo -->
    <div class="w-30 text-2xl font-bold text-primary cursor-pointer select-none">
      <div v-if="mode !== 'dark'">
        <img src="/poqg-white-logo.png" />
      </div>
      <div v-else>
        <img src="/poqg-black-logo.png" />
      </div>
    </div>

    <div class="relative w-full max-w-sm items-center">
      <Input id="search" type="text" placeholder="Search..." class="pl-10" />
      <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
        <Search class="size-4.5 text-muted-foreground" />
      </span>
    </div>

    <div class="flex items-center space-x-4">
      <!-- Botão tema -->
      <button @click="toggleDarkMode" aria-label="Toggle Dark Mode" class="cursor-pointer text-gray-600 dark:text-gray-300 hover:text-primary transition">
        <component :is="darkMode ? Sun : Moon" class="w-6 h-6" />
      </button>

      <!-- Carrinho -->
      <button aria-label="Cart" class="cursor-pointer relative text-gray-600 dark:text-gray-300 hover:text-primary transition">
        <ShoppingCart class="w-6 h-6" />
        <span class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full text-xs w-5 h-5 flex items-center justify-center">
          3
        </span>
      </button>

      <!-- Avatar -->
      <Avatar>
        <AvatarImage src="https://github.com/unovue.png" alt="@unovue" />
        <AvatarFallback>CN</AvatarFallback>
      </Avatar>
    </div>
  </header>

  <div class="border-t border-b border-blue-500 flex justify-center space-x-25
    h-10 px-6 bg-white dark:bg-black text-gray-800 dark:text-gray-300"
  >
    <Button class="h-full flex items-center hover:text-primary transition font-semibold" variant="ghost">Home</Button>
    <Button class="h-full flex items-center hover:text-primary transition font-semibold" variant="ghost">Cards</Button>
    <Button class="h-full flex items-center hover:text-primary transition font-semibold" variant="ghost">Contact</Button>
    <Button class="h-full flex items-center hover:text-primary transition font-semibold" variant="ghost">Events</Button>
  </div>
</template>

