<script lang="ts" setup>
import { ref, onMounted } from "vue";

// let type = "Fairy";

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

const fetchCards = async () => {
  loading.value = true;
  try {
    // const response = await fetch("https://api.pokemontcg.io/v2/cards?q=types:" + type + "&pageSize=30", {
    const response = await fetch(
      "https://api.pokemontcg.io/v2/cards?pageSize=30",
      {
        headers: {},
      }
    );
    const data = await response.json();
    if (data.data) {
      cards.value = shuffleArray(data.data);
    } else {
      cards.value = [];
    }
  } catch (error) {
    console.error("Erro ao buscar cartas:", error);
    cards.value = [];
  } finally {
    loading.value = false;
  }
};

onMounted(fetchCards);
</script>

<template>
  <div class="pt-8 max-w-6xl mx-auto p-3">
    <div v-if="loading" class="flex pt-15 justify-center">
      <img src="/poke.png" class="h-15 animate-spin" />
    </div>

    <div
      v-else-if="cards.length === 0"
      class="text-center pt-15 text-gray-700 text-xl"
    >
      <label> Ops... O Pokémon escapou! </label>
    </div>

    <div
      v-else
      class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-8"
    >
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
