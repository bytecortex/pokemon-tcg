<script setup lang="ts">
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
  DialogClose,
} from "@/components/ui/dialog";
import Label from "./ui/label/Label.vue";
import Separator from "./ui/separator/Separator.vue";
import Button from "@/components/ui/button/Button.vue";
import { X } from "lucide-vue-next";

defineProps<{
  modelValue: boolean;
  card: any;
}>();

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <Dialog
    :open="modelValue"
    @update:open="(val) => emit('update:modelValue', val)"
  >
    <DialogContent class="max-w-[100vh]">
      <DialogClose
        as-child
        class="cursor-pointer absolute top-4 right-4 opacity-70 hover:opacity-100 transition-opacity"
      >
        <X />
      </DialogClose>

      <div class="flex flex-col md:flex-row gap-6 w-full">
        <div class="w-full md:w-1/2">
          <img
            :src="card?.images?.large || card?.images?.small"
            :alt="card?.name ?? 'Desconhecido'"
            class="w-full rounded"
          />
        </div>

        <div class="flex flex-col w-full md:w-1/2">
          <DialogHeader>
            <DialogTitle class="text-[5vh] font-bold">
              {{ card?.name }}
            </DialogTitle>
          </DialogHeader>

          <div class="pt-2">
            <Separator />
          </div>

          <div class="pt-2">
            <Label v-if="card.type" class="text-[2.5vh] font-extralight">
              <span class="font-semibold">Tipo</span>: {{ card?.type }}
            </Label>
            <Label v-if="card.rarity" class="text-[2.5vh] font-extralight">
              <span class="font-semibold">Raridade</span>: {{ card?.rarity }}
            </Label>
            <Label v-if="card.hp" class="text-[2.5vh] font-extralight">
              <span class="font-semibold">HP</span>: {{ card?.hp }}
            </Label>
            <Label v-if="card.id" class="text-[2.5vh] font-extralight">
              <span class="font-semibold">Id</span>: {{ card?.id }}
            </Label>
          </div>

          <div class="pt-2">
            <Separator />
          </div>

          <div class="pt-2">
            <Label v-if="card.price" class="text-[2.5vh] font-extralight">
              <span class="font-semibold">Preço</span>: $ {{ card?.price }}
            </Label>
            <Label v-if="card.stock" class="text-[2.5vh] font-extralight">
              <span class="font-semibold">Estoque</span>: {{ card?.stock }}
            </Label>
          </div>
          
          <DialogFooter class="mt-6 w-full flex justify-center">
            <div class="w-full flex justify-end">
              <Button
                type="button"
                class="mx-auto bg-blue-600 text-white p-[2.5vh] w-full text-[2.5vh] hover:opacity-100 transition-all duration-300 ease-in-out"
                @click=""
                variant="outline"
              >
                Adicionar ao carrinho
              </Button>
            </div>
          </DialogFooter>
        </div>
      </div>
    </DialogContent>
  </Dialog>
</template>
