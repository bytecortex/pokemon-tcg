<script setup lang="ts">
import router from "@/routes"
import { useRoute } from "vue-router"
import Input from "./ui/input/Input.vue"
import Button from "./ui/button/Button.vue"
import { ref, watch, onMounted } from "vue"
import { Sun, Moon, ShoppingCart, Search} from "lucide-vue-next"
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

// Lógica para dark mode
const darkMode = ref(false)

function toggleDarkMode() {
  darkMode.value = !darkMode.value
}

onMounted(() => {
  const savedMode = localStorage.getItem('darkMode')
  if (savedMode === 'true' || savedMode === 'false') {
    darkMode.value = savedMode === 'true'
  } else {
    darkMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
})

watch(darkMode, (newVal) => {
  localStorage.setItem('darkMode', String(newVal))
  if (newVal) {
    document.documentElement.classList.add("dark")
  } else {
    document.documentElement.classList.remove("dark")
  }
})

// Indexamento dos botões
type button = 'Cards' | 'Events' | 'Contact' | 'Home'

function handleClick(origin: button) {
  switch (origin) {
    case 'Cards':
      router.push('/cards')
      break
    case 'Events':
      router.push('/events')
      break
    case 'Contact':
      router.push('/contact')
      break;
    case 'Home':
      router.push('/')
      break
    default:
      router.push('/')
  }
} 

const route = useRoute()

function buttonClass(path: string) {
  if (route.path === path) {
    return [
      'h-8 flex items-center transition font-semibold cursor-pointer text-primary bg-blue-500'
    ];
  }
}
</script>

<template>
  <header class="flex items-center justify-between px-6 py-4 bg-white dark:bg-black shadow-md">
    <!-- Logo -->
    <div class="w-30 text-2xl font-bold text-primary cursor-pointer select-none">
      <div v-if="!darkMode">
        <img src="/poqg-white-logo.png" @click="handleClick('Home')"/>
      </div>
      <div v-else>
        <img src="/poqg-black-logo.png" @click="handleClick('Home')"/>
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
    h-10 py-0.75 bg-white dark:bg-black text-gray-800 dark:text-gray-300"
  >
    <Button 
      @click="handleClick('Home')" 
      :class="buttonClass('/')"
      class="h-8 flex items-center hover:text-primary transition font-semibold cursor-pointer" 
      variant="ghost"
    >
      Home
    </Button>
    <Button 
      @click="handleClick('Cards')" 
      :class="buttonClass('/cards')"
      class="h-8 flex items-center hover:text-primary transition font-semibold cursor-pointer" 
      variant="ghost"
    >
      Cards
    </Button>
    <Button 
      @click="handleClick('Contact')" 
      class="h-8 flex items-center hover:text-primary transition font-semibold cursor-pointer" 
      variant="ghost"
    >
      Contact
    </Button>
    <Button 
      @click="handleClick('Events')"
      class="h-8 flex items-center hover:text-primary transition font-semibold cursor-pointer" 
      variant="ghost"
    >
      Events
    </Button>
  </div>
</template>

