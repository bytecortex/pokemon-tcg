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
          <DialogTitle class="text-xl font-semibold">Sign up</DialogTitle>
        </DialogHeader>

        <div class="flex gap-4">
          <img
            src="/squirtle-full-register.png"
            alt="Side"
            class="w-[200px] h-[200px] self-end scale-x-[-1]"
          />
          <form id="dialogForm" @submit="" class="flex-1 flex flex-col gap-4">
            <FormField v-slot="{ componentField }" name="username">
              <FormItem>
                <FormLabel class="flex justify-end">Name</FormLabel>
                <FormControl>
                  <Input
                    type="text"
                    placeholder="Ash Ketchum"
                    v-bind="componentField"
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="email">
              <FormItem>
                <FormLabel class="flex justify-end">Email</FormLabel>
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
              <FormItem>
                <FormLabel class="flex justify-end">Password</FormLabel>
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
              <Button type="submit" form="dialogForm" class="cursor-pointer">
                Register
              </Button>
            </DialogFooter>
          </form>
        </div>
      </DialogContent>
    </Dialog>
  </Form>
</template>
