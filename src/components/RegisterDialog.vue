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
import { Button } from "./ui/button";
import axios from 'axios';
import { ref } from 'vue';
import { useUserStore } from '@/stores/userStore';


const name = ref('');
const email = ref('');
const password = ref('');
const loading = ref(false);
const userStore = useUserStore();

async function handleRegister() {
  loading.value = true;
  try {
    const response = await axios.post('http://localhost:8000/register', {
      name: name.value,
      email: email.value,
      password: password.value,
    });

    alert(response.data.message);
    // Você pode aqui resetar os campos ou fechar o modal

    name.value = '';
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

      <DialogContent class="sm:max-w-[600px]">
        <DialogClose as-child
          class="cursor-pointer ring-offset-background focus:ring-ring data-[state=open]:bg-accent data-[state=open]:text-muted-foreground absolute top-4 right-4 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:ring-2 focus:ring-offset-2 focus:outline-hidden disabled:pointer-events-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4">
          <X />
          <span class="sr-only">Close</span>
        </DialogClose>

        <DialogHeader class="flex items-center">
          <DialogTitle class="text-xl font-semibold">Sign up</DialogTitle>
        </DialogHeader>

        <div class="flex gap-4">
          <form id="dialogForm" @submit="" class="flex-1 flex flex-col gap-4">
            <FormField v-slot="{ componentField }" name="username">
              <FormItem>
                <FormLabel class="flex">Name</FormLabel>
                <FormControl>
                  <Input type="text" placeholder="Ash Ketchum" v-model="name" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="email">
              <FormItem>
                <FormLabel class="flex">Email</FormLabel>
                <FormControl>
                  <Input type="text" placeholder="example@email.com" v-model="email" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="password">
              <FormItem>
                <FormLabel class="flex">Password</FormLabel>
                <FormControl>
                  <Input type="password" placeholder="••••••••" v-model="password" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>

            <DialogFooter class="pt-2">
              <div class="w-full flex justify-start">
                <Button type="button" @click="handleRegister" :disabled="loading" class="cursor-pointer">
                  {{ loading ? 'Registering...' : 'Register' }}
                </Button>

              </div>
            </DialogFooter>
          </form>
          <img src="/squirtle-full-register.png" alt="Side" class="w-[200px] h-[200px] self-end" />
        </div>
      </DialogContent>
    </Dialog>
  </Form>
</template>
