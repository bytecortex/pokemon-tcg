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
import { ref } from "vue";
import api from "@/api";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { X, Eye, EyeOff } from "lucide-vue-next";
import { useUserStore } from "@/server/userStore";

const name = ref("");
const email = ref("");
const password = ref("");
const loading = ref(false);
const userStore = useUserStore();
const showPassword = ref(false);
const isDialogOpen = ref(false);

async function handleRegister() {
  loading.value = true;
  try {
    const response = await api.post("/register", {
      name: name.value,
      email: email.value,
      password: password.value,
    });

    alert(response.data.message);

    name.value = "";
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
        <DialogTrigger>
          <Button
            type="button"
            class="cursor-pointer"
            @click=""
            variant="outline"
          >
            Sign up
          </Button>
        </DialogTrigger>
      </div>

      <DialogContent class="sm:max-w-[600px]">
        <DialogClose
          as-child
          class="cursor-pointer absolute top-4 right-4 opacity-70 hover:opacity-100 transition-opacity"
        >
          <X />
        </DialogClose>

        <DialogHeader class="flex items-center">
          <DialogTitle class="text-xl font-semibold">Sign up</DialogTitle>
        </DialogHeader>

        <div class="flex gap-4">
          <form id="dialogForm" @submit="" class="flex-1 flex flex-col gap-4">
            <FormField name="username">
              <FormItem>
                <FormLabel class="flex">Name</FormLabel>
                <FormControl>
                  <Input type="text" placeholder="Ash Ketchum" v-model="name" />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField name="email">
              <FormItem>
                <FormLabel class="flex">Email</FormLabel>
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
              <FormItem>
                <FormLabel class="flex">Password</FormLabel>
                <div class="flex">
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
                </div>
                <FormMessage />
              </FormItem>
            </FormField>

            <DialogFooter class="pt-2">
              <div class="w-full flex justify-start">
                <Button
                  type="button"
                  @click="handleRegister"
                  class="cursor-pointer"
                >
                  Register
                </Button>
              </div>
            </DialogFooter>
          </form>
          <img
            src="/squirtle-full-register.png"
            alt="Side"
            class="w-[200px] h-[200px] self-end"
          />
        </div>
      </DialogContent>
    </Dialog>
  </Form>
</template>
