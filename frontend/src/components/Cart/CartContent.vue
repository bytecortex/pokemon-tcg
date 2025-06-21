<script setup lang="ts">
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Minus, Plus, Trash } from "lucide-vue-next";
import api from "@/api";
import { ref, onMounted, computed } from "vue";
import { Button } from "@/components/ui/button/";
import { Label } from "@/components/ui/label/";
import { useUserStore } from "@/server/userStore";
import type { CartItems } from "@/interfaces/carts";
import { Separator } from "@/components/ui/separator";

const userStore = useUserStore();
const userId = userStore.user?.id;

const cartItems = ref<CartItems[]>([]);
const isLoading = ref(true);

// Subtotal computado dinamicamente
const subtotal = computed(() =>
  cartItems.value.reduce((total, item) => total + item.price * item.quantity, 0)
);

// Atualiza a quantidade de um item e sincroniza com o backend
const updateQuantity = async (item: CartItems, change: number) => {
  const newQuantity = item.quantity + change;
  if (newQuantity < 1) return;

  item.quantity = newQuantity;

  try {
    await api.put(`/cart/items/${userId}/${item.id}`, {
      quantity: newQuantity,
    });
  } catch (error) {
    console.error("Erro ao atualizar item:", error);
  }
};

const getCartItems = async () => {
  try {
    const response = await api.get(`/cart/items/${userId}`);
    cartItems.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar carrinho:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  getCartItems();
});
</script>

<template>
  <section class="flex flex-col lg:flex-row justify-center p-6 gap-6">
    <!-- Coluna de itens -->
    <Card class="w-full lg:w-200">
      <CardContent>
        <CardTitle class="text-4xl pb-3 font-bold">Cart</CardTitle>
        <div v-if="isLoading">Carregando...</div>
        <div v-else-if="cartItems.length === 0">Carrinho vazio.</div>
        <div v-else class="flex flex-col">
          <div v-for="ci in cartItems" :key="ci.id">
            <div class="py-2">
              <Separator />
            </div>
            <div class="gap-x-3 flex">
              <figure>
                <img class="w-32" :src="ci.image_url" alt="" />
              </figure>
              <div class="flex justify-between w-full">
                <dl>
                  <dt class="font-semibold text-xl pb-1">{{ ci.name }}</dt>
                  <div
                    class="flex items-center justify-between border-2 border-blue-600 h-8 w-24 rounded-2xl"
                  >
                    <span
                      @click="updateQuantity(ci, -1)"
                      class="cursor-pointer px-2"
                    >
                      <Minus :size="16" />
                    </span>
                    <Label class="font-semibold text-md">
                      {{ ci.quantity }}
                    </Label>
                    <span
                      @click="updateQuantity(ci, 1)"
                      class="cursor-pointer px-2"
                    >
                      <Plus :size="16" />
                    </span>
                  </div>
                </dl>

                <div class="flex items-center">
                  <Label class="font-semibold text-xl">
                    $ {{ ci.price.toFixed(2) }}
                  </Label>
                </div>
              </div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>

    <!-- Coluna de subtotal -->
    <div>
      <Card class="w-full lg:w-110">
        <CardContent>
          <CardTitle class="text-2xl font-semibold">
            Subtotal ({{ cartItems.length }} produtos):
          </CardTitle>
          <p class="text-2xl font-semibold">$ {{ subtotal.toFixed(2) }}</p>
        </CardContent>
        <CardFooter>
          <div class="pt-2 w-full flex justify-end">
            <Button
              type="button"
              @click=""
              class="rounded-xl text-lg h-12 w-full bg-blue-600 text-white border border-blue-600 hover:bg-transparent hover:text-blue-600 transition-all duration-300 ease-in-out"
            >
              Fechar pedido
            </Button>
          </div>
        </CardFooter>
      </Card>
    </div>
  </section>
</template>
