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
</script>

<template>
  <Form>
    <Dialog>
      <DialogTrigger>
        <Avatar class="cursor-pointer" @click="">
          <AvatarImage src="https://github.com/unovue.png" alt="@unovue" />
          <AvatarFallback>CN</AvatarFallback>
        </Avatar>
      </DialogTrigger>

      <DialogContent class="sm:max-w-[600px]">
        <DialogClose
          as-child
          class="cursor-pointer ring-offset-background focus:ring-ring data-[state=open]:bg-accent data-[state=open]:text-muted-foreground absolute top-4 right-4 rounded-xs opacity-70 transition-opacity hover:opacity-100 focus:ring-2 focus:ring-offset-2 focus:outline-hidden disabled:pointer-events-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
        >
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
                  <Input
                    type="text"
                    placeholder="example@email.com"
                    v-bind="componentField"
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="password">
              <FormItem class="pt-2">
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input
                    type="text"
                    placeholder="••••••••"
                    v-bind="componentField"
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>

            <DialogFooter class="pt-2">
              <div class="flex justify-start w-full">
                <Button type="submit" form="dialogForm" class="cursor-pointer">
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
