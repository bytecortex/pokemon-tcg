// src/stores/userStore.ts
import { defineStore } from "pinia";
import { ref, watch } from "vue";

export const useUserStore = defineStore("user", () => {
  const user = ref<{ id: number; name: string; email: string } | null>(
    JSON.parse(localStorage.getItem("user") || "null")
  );

  function setUser(newUser: { id: number; name: string; email: string }) {
    user.value = newUser;
  }

  function logout() {
    user.value = null;
  }

  watch(
    user,
    (newUser) => {
      if (newUser) {
        localStorage.setItem("user", JSON.stringify(newUser));
      } else {
        localStorage.removeItem("user");
      }
    },
    { deep: true }
  );

  return { user, setUser, logout };
});
