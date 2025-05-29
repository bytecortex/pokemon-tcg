<script setup lang="ts">
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { SlidersHorizontal, ArrowDownUp } from "lucide-vue-next";
</script>

<template>
  <div
    class="flex justify-start items-center shadow-md w-full h-16 pt-2 px-4 bg-white dark:bg-black text-gray-800 dark:text-gray-300"
  >
    <!-- Filtrar cartas -->
    <div class="flex">
      <Sheet>
        <SheetTrigger as-child>
          <Button class="cursor-pointer" variant="outline">
            <SlidersHorizontal />
            Filters
          </Button>
        </SheetTrigger>
        <SheetContent side="left">
          <SheetHeader>
            <SheetTitle>Edit profile</SheetTitle>
            <SheetDescription>
              Make changes to your profile here. Click save when you're done.
            </SheetDescription>
          </SheetHeader>
          <div class="grid gap-4 py-4">
            <div class="grid grid-cols-4 items-center gap-4">
              <Label for="name" class="text-right"> Name </Label>
              <Input
                id="name"
                default-value="Pedro Duarte"
                class="col-span-3"
              />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
              <Label for="username" class="text-right"> Username </Label>
              <Input
                id="username"
                default-value="@peduarte"
                class="col-span-3"
              />
            </div>
          </div>
          <SheetFooter>
            <SheetClose as-child>
              <Button type="submit">Save changes</Button>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>

    <!-- Ordenar -->
    <div class="flex pl-2">
      <Button class="cursor-pointer" variant="outline">
        <ArrowDownUp />
        Sort
      </Button>
    </div>
  </div>
</template>
