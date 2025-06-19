import { ref } from "vue";
import type { Card } from "@/interfaces/cards"; 
import api from "@/api";

export function useCards() {
  const cards = ref<Card[]>([]);
  const loading = ref(false);

  const fetchCards = async (query: { name?: string; types?: string }) => {
    loading.value = true;
    try {
      const params = new URLSearchParams();
      if (query.name) params.append("name", query.name);
      if (query.types) params.append("types", query.types);

      const response = await api.get(`/cards?${params.toString()}`);
      cards.value = response.data;
    } catch (error) {
      console.error("Erro ao buscar cartas:", error);
      cards.value = [];
    } finally {
      loading.value = false;
    }
  };

  return { cards, loading, fetchCards };
}