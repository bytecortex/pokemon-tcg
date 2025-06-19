<script lang="ts" setup>
import { useRoute } from "vue-router";
import { onMounted, watch } from "vue";
import { useCards } from "@/composables/useCards";

const route = useRoute();
const { cards, loading, fetchCards } = useCards();

onMounted(() => {
  fetchCards({ name: route.query.name as string, types: route.query.types as string });
});

watch(
  () => [route.query.name, route.query.types],
  () => {fetchCards({ name: route.query.name as string, types: route.query.types as string });}
);

const adicionarAoCarrinho = () => {
  console.log(`Adicionado ao carrinho:`);
};
</script>

<template>
  <section class="pt-8 max-w-6xl mx-auto p-3">
    <!-- Carregando -->
    <div v-if="loading" class="flex pt-15 justify-center">
      <img src="/poke.png" class="h-15 animate-spin" />
    </div>
    <!-- Sem Resultados -->
    <div v-else-if="cards.length === 0" class="text-center pt-15 text-gray-700 text-xl">
      <label> Ops... O Pokémon escapou! </label>
    </div>
    <!-- Lista de cartas -->
    <ul v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-8" role="list">
      <li v-for="card in cards" :key="card.id" class="cursor-pointer w-full h-auto object-contain rounded-md text-center">
        <!-- Imagem -->
        <figure>
          <img :src="card.images.small" :alt="card.name" class="w-full h-auto mb-2" />
        </figure>
        <!-- Detalhes -->
        <div class="px-4 pb-4 text-sm">
          <p class="mb-1">{{ card.name}}</p>
          <p class="mb-1">{{ card.rarity || 'No rarity' }}</p>
          <p class="mb-1">{{ card.series || 'No series' }}</p>
          <p class="mb-1">{{ card.price?.toFixed(2) || 'No price'}}</p>

          <!-- Botão COMPRAR (no tema claro n ta legal) -->
          <button class="cursor-pointer mt-3 w-full bg-blue-500 hover:bg-blue-600 py-1.5 rounded transition text-sm" @click="adicionarAoCarrinho()">
            Comprar
          </button>
        </div>
      </li>
    </ul>
  </section>
</template>
