<script setup lang="ts">
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogClose,
} from "@/components/ui/dialog";
import api from '@/api';
import { ref, watch } from 'vue';
import { X } from "lucide-vue-next";

const props = defineProps<{ orderId: number | null; open: boolean }>();
const emit = defineEmits(['close']);

const cards = ref<any[]>([]);
const loading = ref(false);

watch(
  () => [props.open, props.orderId],
  async ([isOpen, orderId]) => {
    if (isOpen && orderId !== null) {
      loading.value = true;
      try {
        const { data } = await api.get(`/orders/${orderId}/cards`);
        cards.value = data;
      } catch (e) {
        console.error('Erro ao carregar cartas:', e);
        cards.value = [];
      } finally {
        loading.value = false;
      }
    } else {
      cards.value = [];
    }
  },
  { immediate: true }
);
</script>

<template>
  <Dialog
    :open="open"
    @update:open="val => { if (!val) emit('close'); }"
  >
    <DialogContent class="max-w-3xl w-full">
      <DialogClose
        as-child
        class="cursor-pointer absolute top-4 right-4 opacity-70 hover:opacity-100 transition-opacity"
      >
        <X />
      </DialogClose>

      <DialogHeader>
        <DialogTitle class="text-2xl font-bold">
          Detalhes do Pedido #{{ orderId }}
        </DialogTitle>
      </DialogHeader>

      <section class="mt-4">
        <div v-if="loading" class="text-center py-10 text-gray-500">
          Carregando cartas...
        </div>

        <div v-else-if="cards.length === 0" class="text-center py-10 text-gray-500">
          Nenhuma carta encontrada.
        </div>

        <div v-else class="grid grid-cols-2 md:grid-cols-3 gap-4">
          <div
            v-for="card in cards"
            :key="card.card_id"
            class="border rounded-md p-3 shadow-sm flex flex-col items-center"
          >
            <img
              :src="card.image_url_small"
              :alt="card.name"
              class="w-full max-w-[120px] mb-2"
            />
            <div class="text-center font-semibold text-sm">{{ card.name }}</div>
            <div class="text-xs text-gray-500">Qtd: {{ card.quantity }}</div>
            <div class="text-xs text-gray-500">ID: {{ card.card_id }}</div> 
          </div>
        </div>
      </section>

      <DialogFooter class="mt-6 flex justify-end">
        <button
          @click="$emit('close')"
          class="bg-gray-600 text-white px-4 py-2 rounded hover:bg-gray-700 transition"
        >
          Fechar
        </button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
