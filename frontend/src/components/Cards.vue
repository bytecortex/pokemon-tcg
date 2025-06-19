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
