<script lang="ts" setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";

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
    const query = route.query.q as string | undefined;
    let url = "https://api.pokemontcg.io/v2/cards?pageSize=30";

    if (query) {
      url = `https://api.pokemontcg.io/v2/cards?q=name:"${encodeURIComponent(
        query
      )}"&pageSize=30`;
    }

    const response = await fetch(url, { headers: {} });
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

watch(
  () => route.query.q,
  () => {
    fetchCards();
  }
);
</script>

<template>
  <div class="pt-3 p-3">
    <div v-if="loading" class="flex pt-15 justify-center">
      <img src="/poke.png" class="h-15 animate-spin" />
    </div>

    <div
      v-else-if="cards.length === 0"
      class="text-center pt-15 text-gray-700 text-xl"
    >
      <div class="block">
        <Label class="text-2xl font-semibold">Ops... O Pokémon escapou!</Label>
        <Label class="text-xl font-semibold">
          <br />Parece que o seu Pokémon não foi encontrado em nossa base de
          dados.
        </Label>
      </div>
    </div>

    <div
      v-else
      class="grid gap-4"
      style="grid-template-columns: repeat(auto-fit, minmax(150px, 1fr))"
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
