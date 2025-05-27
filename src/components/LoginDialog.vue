<script setup lang="ts">
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  Dialog,
  DialogTitle,
  DialogTrigger,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogClose,
} from "@/components/ui/dialog";
import {
  Form,
  FormField,
  FormLabel,
  FormControl,
  FormItem,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "./ui/input";
import { X } from "lucide-vue-next";
import { Label } from "./ui/label";
import { Button } from "./ui/button";
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/userStore';

const email = ref('');
const password = ref('');
const loading = ref(false);
const userStore = useUserStore();

async function handleLogin() {
  loading.value = true;
  try {
    const response = await axios.post('http://localhost:8000/login', {
      email: email.value,
      password: password.value,
    });

    alert(response.data.message);

    userStore.setUser(response.data.user);

    email.value = '';
    password.value = '';

  } catch (error: any) {
    if (error.response) {
      alert(error.response.data.detail);
    } else {
      alert('An error occurred');
    }
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <Form>
    <Dialog>
      <div v-if="!userStore.user">
        <DialogTrigger>
          <Avatar class="cursor-pointer" @click="">
            <AvatarImage src="https://github.com/unovue.png" alt="@unovue" />
            <AvatarFallback>CN</AvatarFallback>
          </Avatar>
        </DialogTrigger>
      </div>
      <span v-if="userStore.user" class="font-medium cursor-pointer hover:underline" @click="userStore.logout()"
        title="Logout">
        {{ userStore.user.name }}
      </span>

      <DialogContent class="sm:max-w-[600px]">
        <DialogClose as-child
          class="cursor-pointer ring-offset-background focus:ring-ring data-[state=open]:bg-accent data-[state=open]:text-muted-foreground absolute top-4 right-4 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:ring-2 focus:ring-offset-2 focus:outline-hidden disabled:pointer-events-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4">
          <X />
          <span class="sr-only">Close</span>
        </DialogClose>

        <DialogHeader class="flex items-center">
          <DialogTitle class="text-xl font-semibold">Sign in</DialogTitle>
        </DialogHeader>

        <div class="flex gap-4">
          <form id="dialogForm" @submit="" class="flex-1 flex flex-col gap-4">
            <FormField v-slot="{ componentField }" name="username">
              <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl>
                  <Input type="text" placeholder="example@email.com" v-model="email" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="password">
              <FormItem class="pt-2">
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input type="password" placeholder="••••••••" v-model="password" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>

            <DialogFooter class="pt-2">
              <div class="flex justify-start w-full">
                <Button type="button" @click="handleLogin" :disabled="loading" class="cursor-pointer">
                  {{ loading ? 'Logging in...' : 'Log in' }}
                </Button>
              </div>
            </DialogFooter>
          </form>
          <img src="/pikachu-full-login.png" alt="Side" class="w-[200px] h-[200px]" />
        </div>
      </DialogContent>
    </Dialog>
  </Form>
</template>
