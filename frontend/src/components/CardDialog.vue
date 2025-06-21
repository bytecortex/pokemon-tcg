<script setup lang="ts">
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogClose,
} from "@/components/ui/dialog";
import Separator from "./ui/separator/Separator.vue";
import Button from "@/components/ui/button/Button.vue";
import { X } from "lucide-vue-next";

const validTypes = [
  "bug",
  "darkness",
  "dragon",
  "lightning",
  "fairy",
  "fighting",
  "fire",
  "flying",
  "ghost",
  "grass",
  "ground",
  "ice",
  "metal",
  "colorless",
  "poison",
  "psychic",
  "rock",
  "water",
];

const validSubtypes = ["ex", "gx", "vmax"];

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
      <section class="flex flex-col md:flex-row gap-6 w-full">
        <!-- Carta -->
        <figure class="w-full md:w-1/2 flex items-center justify-center">
          <img
            :src="card?.images?.large || card?.images?.small"
            :alt="card?.name ?? 'Undefined'"
            class="w-full rounded"
          />
        </figure>
        <!-- Informações -->
        <aside class="flex flex-col w-full md:w-1/2">
          <DialogHeader>
            <DialogTitle class="text-[5vh] font-bold">
              {{ card?.name }}
              <img
                v-if="
                  card.types && validTypes.includes(card.types.toLowerCase())
                "
                class="max-w-[5vh] inline mb-2"
                :src="'/types/' + card.types.toLowerCase() + '.svg'"
                :alt="card.types"
              />
            </DialogTitle>
            <!-- Texto Descritivo -->
            <span class="text-[2vh]">{{ card.flavor_text }}</span>
          </DialogHeader>

          <div class="pt-2">
            <Separator />
          </div>

          <!-- Detalhes de atributo -->
          <dl class="pt-2 text-[2.5vh] font-extralight space-y-1">
            <div v-if="card.id" class="flex">
              <dt class="font-semibold">Id:</dt>
              <dd class="ml-2">{{ card.id }}</dd>
            </div>
            <div v-if="card.supertype" class="flex">
              <dt class="font-semibold">Supertype:</dt>
              <dd class="ml-2">{{ card.supertype }}</dd>
            </div>
            <div v-if="card.subtypes" class="flex">
              <dt class="font-semibold">Subtypes:</dt>
              <dd class="ml-2">{{ card.subtypes }}</dd>
            </div>
            <div v-if="card.rarity" class="flex">
              <dt class="font-semibold">Rarity:</dt>
              <dd class="ml-2">{{ card.rarity }}</dd>
            </div>
            <div v-if="card.types" class="flex">
              <dt class="font-semibold">Tipo:</dt>
              <dd class="ml-2">{{ card.types }}</dd>
            </div>
            <div v-if="card.hp" class="flex">
              <dt class="font-semibold">HP:</dt>
              <dd class="ml-2">{{ card.hp }}</dd>
            </div>
          </dl>

          <div
            v-if="
              card.subtypes &&
              card.subtypes
                .split(',')
                .some((sub) => validSubtypes.includes(sub.trim().toLowerCase()))
            "
          >
            <div class="pt-2">
              <Separator />
            </div>

            <div class="flex items-center gap-2 flex-wrap">
              <span v-if="card.subtypes && Array.isArray(card.subtypes)">
                <img
                  class="max-w-[5vh] inline mb-2 ml-2"
                  :src="'subtypes/' + card.subtypes.toLowerCase() + '.png'"
                  :alt="subtypes"
                />
              </span>
            </div>
          </div>

          <div class="pt-2">
            <Separator />
          </div>

          <!-- Detalhes comerciais -->
          <dl class="pt-2 text-[2.5vh] font-extralight space-y-1">
            <div v-if="card.price" class="flex">
              <dt class="font-semibold">Price:</dt>
              <dd class="ml-2">$ {{ card.price.toFixed(2) }}</dd>
            </div>
            <div v-if="card.stock" class="flex">
              <dt class="font-semibold">Stock:</dt>
              <dd class="ml-2">{{ card.stock }}</dd>
            </div>
          </dl>

          <!-- Adicionar ao Carrinho -->
          <DialogFooter class="mt-auto w-full flex justify-center">
            <div class="pt-2 w-full flex justify-end">
              <Button
                type="button"
                @click=""
                class="mx-auto w-full p-[2.5vh] text-[2.5vh] bg-blue-600 text-white border border-blue-600 hover:bg-transparent hover:text-blue-600 transition-all duration-300 ease-in-out"
              >
                Adicionar ao carrinho
              </Button>
            </div>
          </DialogFooter>
        </aside>
      </section>
    </DialogContent>
  </Dialog>
</template>

<style></style>
