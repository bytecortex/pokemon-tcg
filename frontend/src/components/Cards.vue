<script lang="ts" setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import { onMounted, watch } from "vue";
import { useCards } from "@/composables/useCards";
import CardDialog from "@/components/CardDialog.vue";

const route = useRoute();
const { cards, loading, fetchCards } = useCards();
const selectedCard = ref(null);
const showDialog = ref(false);

const openCardDialog = (card: any) => {
  selectedCard.value = card;
  showDialog.value = true;
};

onMounted(() => {
  fetchCards({
    name: route.query.name as string,
    types: route.query.types as string,
    in_stock_only: route.query.in_stock_only === 'true',
  });
});

watch(
  () => [route.query.name, route.query.types, route.query.in_stock_only],
  () => {
    fetchCards({
      name: route.query.name as string,
      types: route.query.types as string,
      in_stock_only: route.query.in_stock_only === 'true',
    });
  }
);
</script>

<template>
  <section class="pt-8 max-w-6xl mx-auto p-3">
    <!-- Carregando -->
    <div v-if="loading" class="flex pt-15 justify-center">
      <img src="/poke.png" class="h-15 animate-spin" />
    </div>
    <!-- Sem Resultados -->
    <div
      v-else-if="cards.length === 0"
      class="text-center pt-15 text-gray-700 text-xl"
    >
      <label> Ops... O Pokémon escapou! </label>
    </div>
    <!-- Lista de cartas -->
    <ul
      v-else
      class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-8"
      role="list"
    >
      <li
        v-for="card in cards"
        :key="card.id"
        class="cursor-pointer w-full h-auto object-contain rounded-md text-center"
      >
        <!-- Imagem -->
        <figure @click="openCardDialog(card)">
          <img
            :src="card.images.small"
            :alt="card.name"
            class="w-full h-auto mb-2"
          />
        </figure>
      </li>
    </ul>
  </section>
  <CardDialog v-if="selectedCard" v-model="showDialog" :card="selectedCard" />
</template>
