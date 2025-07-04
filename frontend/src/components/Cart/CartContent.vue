<script setup lang="ts">
import {
  Card,
  CardContent,
  CardFooter,
  CardTitle,
} from "@/components/ui/card";
import { Minus, Plus } from "lucide-vue-next";
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

// Total computado dinamicamente
const total = computed(() =>
  cartItems.value.reduce((total, item) => total + item.price * item.quantity, 0)
);

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

const updateQuantity = async (itemId: number, newQuantity: number) => {
  if (newQuantity < 1) {
    // Opcional: confirmar remoção
    const confirmRemove = confirm("Deseja remover este item do carrinho?");
    if (!confirmRemove) return;
  }

  try {
    await api.put(`/cart/update_quantity/${itemId}`, {
      quantity: newQuantity,
    });

    // Atualiza localmente sem recarregar tudo
    const item = cartItems.value.find(item => item.id === itemId);
    if (item) {
      if (newQuantity < 1) {
        cartItems.value = cartItems.value.filter(item => item.id !== itemId);
      } else {
        item.quantity = newQuantity;
      }
    }
  } catch (error) {
    console.error("Erro ao atualizar quantidade:", error);
  }
};

// CHECKOUT
const isProcessingOrder = ref(false);

const checkout = async () => {
  if (cartItems.value.length === 0) {
    alert("Carrinho vazio.");
    return;
  }

  isProcessingOrder.value = true;

  try {
    await api.post(`/cart/checkout/${userId}`);
    alert("Pedido finalizado com sucesso!");
    cartItems.value = []; // limpa o carrinho
  } catch (error: any) {
    const detail = error?.response?.data?.detail || "Erro ao finalizar o pedido.";
    alert(detail);
  } finally {
    isProcessingOrder.value = false;
  }
};
// FIM CHECKOUT

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
          <template v-for="cartItem in cartItems" :key="cartItem.id">
            <div class="py-2">
              <Separator />
            </div>
            <div class="gap-x-3 flex">
              <figure>
                <img class="w-32" :src="cartItem.image_url" alt="" />
              </figure>
              <div class="flex justify-between w-full">
                <dl>
                  <dt class="font-semibold text-xl pb-1">{{ cartItem.name }}</dt>
                  <div class="flex items-center justify-between border-2 border-blue-600 h-8 w-24 rounded-2xl">
                    <span @click="updateQuantity(cartItem.id, cartItem.quantity - 1)" class="cursor-pointer px-2">
                      <Minus :size="16" />
                    </span>
                    <Label class="font-semibold text-md">
                      {{ cartItem.quantity }}
                    </Label>
                    <span @click="updateQuantity(cartItem.id, cartItem.quantity + 1)" class="cursor-pointer px-2">
                      <Plus :size="16" />
                    </span>
                  </div>
                </dl>

                <div class="flex items-center flex-col justify-center text-right">
                  <Label class="font-semibold text-sm text-gray-500">
                    $ {{ cartItem.price.toFixed(2) }} ea
                  </Label>
                  <Label class="font-semibold text-xl">
                    $ {{ (cartItem.price * cartItem.quantity).toFixed(2) }}
                  </Label>
                </div>
              </div>
            </div>
          </template>
        </div>
      </CardContent>
    </Card>

    <!-- Coluna de Total -->
    <div>
      <Card class="w-full lg:w-110">
        <CardContent>
          <CardTitle class="text-2xl font-semibold">
            Total ({{ cartItems.length }} items):
          </CardTitle>
          <p class="text-2xl font-semibold">$ {{ total.toFixed(2) }}</p>
        </CardContent>
        <CardFooter>
          <div class="pt-2 w-full flex justify-end">
            <Button type="button" :disabled="isProcessingOrder" @click="checkout"
              class="rounded-xl text-lg h-12 w-full bg-blue-600 text-white border border-blue-600 hover:bg-transparent hover:text-blue-600 transition-all duration-300 ease-in-out">
              {{ isProcessingOrder ? 'Processing...' : 'Complete Order' }}
            </Button>
          </div>
        </CardFooter>
      </Card>
    </div>
  </section>
</template>
