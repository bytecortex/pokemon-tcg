import { defineStore } from "pinia";
import { ref, watch } from "vue";

export const useUserStore = defineStore("user", () => {
  const user = ref<{ id: number; name: string; email: string; role: string } | null>(
    JSON.parse(localStorage.getItem("user") || "null")
  );
  const token = ref<string | null>(localStorage.getItem("token") || null);

  function setUser(newUser: { id: number; name: string; email: string; role: string }, newToken: string) {
    user.value = newUser;
    token.value = newToken;
  }

  function logout() {
    user.value = null;
    token.value = null;
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

  watch(token, (newToken) => {
    if (newToken) {
      localStorage.setItem("token", newToken);
    } else {
      localStorage.removeItem("token");
    }
  });

  return { user, token, setUser, logout };
});
