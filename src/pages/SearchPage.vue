<script setup lang='ts'>
import Header from '@/components/Header.vue';
import { useRoute } from 'vue-router';
import { ref, computed, watch, onMounted } from 'vue';

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
  set?: CardSet;
}

const route = useRoute();
const query = computed(() => (route.query.q ?? '').toString());

const cards = ref<Card[]>([]);
const loading = ref(false);
const error = ref('');

async function fetchCards(searchTerm: string) {
  if (!searchTerm.trim()) {
    cards.value = [];
    return;
  }

  loading.value = true;
  error.value = '';

  try {
    cards.value = [];
    const response = await fetch(`https://api.pokemontcg.io/v2/cards?q=name:"${encodeURIComponent(searchTerm)}"&pageSize=30`);
    if (!response.ok) throw new Error('Erro na requisição');
    const data = await response.json();
    cards.value = data.data; // o array de cards está na propriedade 'data'
  } catch (err: any) {
    error.value = err.message || 'Erro desconhecido';
  } finally {
    loading.value = false;
  }
}

watch(query, (newQuery) => {
  fetchCards(newQuery);
});

onMounted(() => {
  fetchCards(query.value);
});

</script>

<template>
  <Header />
  <div>
    <h1>Resultados para: "{{ query }}"</h1>

    <div v-if="loading" class="flex pt-15 justify-center">
      <img src="/poke.png" class="h-15 animate-spin">
    </div>
    <div v-if="error" class="text-red-500">{{ error }}</div>

    <div v-if="cards.length === 0 && !loading && !error">
      Nenhum card encontrado.
    </div>

    <div class="pt-8 max-w-6xl mx-auto p-3">
      <div v-if="cards.length > 0" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-8">
        <img v-for="card in cards" :key="card.id" :src="card.images.small" :alt="card.name"
          class="w-full h-auto object-contain rounded-md" />
      </div>
    </div>
  </div>
</template>