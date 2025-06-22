import { ref } from "vue";
import type { Card } from "@/interfaces/cards"; 
import api from "@/api";

export function useCards() {
  const cards = ref<Card[]>([]);
  const loading = ref(false);

  const fetchCards = async (query: { name?: string; types?: string; in_stock_only?: boolean; hyper_rare?: boolean}) => {
    loading.value = true;
    try {
      const params = new URLSearchParams();
      if (query.name) params.append("name", query.name);
      if (query.types) params.append("types", query.types);
      if (query.in_stock_only !== undefined) {
        params.append("in_stock_only", String(query.in_stock_only));
      }
      if (query.hyper_rare !== undefined) {
        params.append("hyper_rare", String(query.hyper_rare));
      }

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
