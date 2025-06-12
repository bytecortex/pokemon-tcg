<script lang="ts" setup>
import { useRoute } from "vue-router";
import { ref, onMounted, watch } from "vue";

interface CardImage {
  small: string;
  large?: string;
}

interface CardSet {
  id: string;
  name: string;
}

interface Card {
  id: string;
  name: string;
  images: CardImage;
  set: CardSet;
}

const cards = ref<Card[]>([]);
const loading = ref(false);

function shuffleArray<T>(array: T[]): T[] {
  const arr = array.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

const route = useRoute();

const fetchCards = async () => {
  loading.value = true;
  try {
    const queryName = route.query.q as string | undefined;
    const queryTypes = route.query.types as string | undefined;

    let queryParts: string[] = [];

    if (queryName) queryParts.push(`name:"${queryName}"`);
    if (queryTypes) queryParts.push(`types:"${queryTypes}"`);

    let url = "https://api.pokemontcg.io/v2/cards?pageSize=30";

    if (queryParts.length > 0) {
      const queryString = encodeURIComponent(queryParts.join(" "));
      url = `https://api.pokemontcg.io/v2/cards?q=${queryString}&pageSize=30`;
    }

    const response = await fetch(url);
    const data = await response.json();

    cards.value = data.data ? shuffleArray(data.data) : [];
  } catch (error) {
    console.error("Erro ao buscar cartas:", error);
    cards.value = [];
  } finally {
    loading.value = false;
  }
};

onMounted(fetchCards);

watch(
  () => [route.query.q, route.query.types],
  () => {
    fetchCards();
  }
);
</script>

<template>
  <div class="pt-8 max-w-6xl mx-auto p-3">
    <div v-if="loading" class="flex pt-15 justify-center">
      <img src="/poke.png" class="h-15 animate-spin" />
    </div>

    <div v-else-if="cards.length === 0" class="text-center pt-15 text-gray-700 text-xl">
      <label> Ops... O Pokémon escapou! </label>
    </div>

    <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-8">
      <img
        v-for="card in cards"
        :key="card.id"
        :src="card.images.small"
        :alt="card.name"
        class="cursor-pointer w-full h-auto object-contain rounded-md"
      />
    </div>
  </div>
</template>
