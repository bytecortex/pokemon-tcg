<script setup lang="ts">
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
import { X, Eye, EyeOff } from "lucide-vue-next";
import { Button } from "./ui/button";
import api from "@/api";
import { ref } from "vue";
import { useUserStore } from "@/server/userStore";

const email = ref("");
const password = ref("");
const loading = ref(false);
const showPassword = ref(false);
const userStore = useUserStore();
const isDialogOpen = ref(false);

async function handleLogin() {
  loading.value = true;
  try {
    const response = await api.post("/login", {
      email: email.value,
      password: password.value,
    });

    alert(response.data.message);

    userStore.setUser(response.data.user);

    email.value = "";
    password.value = "";
    isDialogOpen.value = false;
  } catch (error: any) {
    if (error.response) {
      const detail = error.response.data.detail;

      if (Array.isArray(detail)) {
        const messages = detail.map((err: any) => {
          const field = err.loc[1] ?? "Field";
          return `${field}: ${err.msg}`;
        });
        alert(messages.join("\n"));
      } else if (typeof detail === "string") {
        alert(detail);
      } else {
        alert("Unknown error.");
      }
    } else {
      alert("An unexpected error has occurred.");
    }
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <Form>
    <Dialog v-model:open="isDialogOpen">
      <div v-if="!userStore.user">
        <DialogTrigger as-child>
          <Button type="button" @click="isDialogOpen = true">Log in</Button>
        </DialogTrigger>
      </div>
      <span
        v-if="userStore.user"
        class="font-medium cursor-pointer hover:underline"
        @click="userStore.logout()"
        title="Logout"
      >
        {{ userStore.user.name }}
      </span>

      <DialogContent class="sm:max-w-[600px]">
        <DialogClose
          as-child
          class="cursor-pointer absolute top-4 right-4 opacity-70 hover:opacity-100 transition-opacity"
        >
          <X />
        </DialogClose>

        <DialogHeader class="flex items-center">
          <DialogTitle class="text-xl font-semibold">Sign in</DialogTitle>
        </DialogHeader>

        <div class="flex gap-4">
          <form id="dialogForm" @submit="" class="flex-1 flex flex-col gap-4">
            <FormField name="username">
              <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl>
                  <Input
                    type="text"
                    placeholder="example@email.com"
                    v-model="email"
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField name="password">
              <FormItem class="pt-2">
                <FormLabel>Password</FormLabel>
                <FormControl class="relative w-full">
                  <div class="relative w-full">
                    <Input
                      :type="showPassword ? 'text' : 'password'"
                      placeholder="••••••••"
                      v-model="password"
                      class="pr-10"
                    />
                    <span
                      class="cursor-pointer absolute inset-y-0 right-2 flex items-center justify-start px-2"
                      @click="showPassword = !showPassword"
                    >
                      <component
                        :is="showPassword ? EyeOff : Eye"
                        class="size-5 text-muted-foreground"
                      />
                    </span>
                  </div>
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>

            <DialogFooter class="pt-2">
              <div class="flex justify-start w-full">
                <Button
                  type="button"
                  @click="handleLogin"
                  :disabled="loading"
                  class="cursor-pointer"
                >
                  Log in
                </Button>
              </div>
            </DialogFooter>
          </form>
          <img
            src="/pikachu-full-login.png"
            alt="Side"
            class="w-[200px] h-[200px]"
          />
        </div>
      </DialogContent>
    </Dialog>
  </Form>
</template>
