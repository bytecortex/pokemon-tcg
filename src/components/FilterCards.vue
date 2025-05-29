<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Separator } from "@/components/ui/separator";
import { SlidersHorizontal, ArrowDownUp } from "lucide-vue-next";
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

const types = [
  "Colorless",
  "Darkness",
  "Dragon",
  "Fairy",
  "Fighting",
  "Fire",
  "Grass",
  "Lightning",
  "Metal",
  "Psychic",
  "Water",
];

const selectedTypes = ref<string[]>([]);

const router = useRouter();
const route = useRoute();

function syncSelectedTypesFromQuery() {
  const f = route.query.f as string | undefined;
  if (f) {
    selectedTypes.value = f.split(",").filter((t) => types.includes(t));
  } else {
    selectedTypes.value = [];
  }
}

function filterCards() {
  router.push({
    path: "/cards",
    query: {
      ...route.query,
      f: selectedTypes.value.join(","),
    },
  });
}

function clearFilters() {
  selectedTypes.value = [];
  const { f, ...rest } = route.query;
  router.push({
    path: "/cards",
    query: rest,
  });
}

onMounted(() => {
  syncSelectedTypesFromQuery();
});

watch(
  () => route.query.f,
  () => {
    syncSelectedTypesFromQuery();
  }
);

function toggleType(type: string) {
  if (selectedTypes.value.includes(type)) {
    selectedTypes.value = selectedTypes.value.filter((t) => t !== type);
  } else {
    selectedTypes.value = [...selectedTypes.value, type];
  }
}
</script>

<template>
  <div
    class="flex justify-start items-center w-full h-16 pt-3 px-4 bg-white dark:bg-black text-gray-800 dark:text-gray-300 shadow-md space-x-4"
  >
    <Sheet>
      <SheetTrigger as-child>
        <Button variant="outline">
          <SlidersHorizontal />
          Filters
        </Button>
      </SheetTrigger>

      <SheetContent side="left" class="flex flex-col h-full">
        <SheetHeader class="shrink-0">
          <SheetTitle class="text-xl">Filters</SheetTitle>
          <SheetDescription>
            Use the filters below to customize the displayed cards.
          </SheetDescription>
        </SheetHeader>

        <div class="overflow-y-auto px-4 py-2 space-y-2 flex-1">
          <Separator />
          <label class="font-semibold text-lg">Type</label>

          <div
            v-for="type in types"
            :key="type"
            class="flex items-center space-x-2 pt-2"
          >
            <Checkbox
              class="cursor-pointer"
              :id="`type-${type}`"
              :checked="selectedTypes.includes(type)"
              @change="toggleType(type)"
            />
            <label
              :for="`type-${type}`"
              class="text-md font-medium leading-none cursor-pointer"
            >
              {{ type }}
            </label>
          </div>
        </div>

        <SheetFooter class="shrink-0 px-4 pb-4 space-x-2">
          <SheetClose as-child>
            <Button class="text-md" type="button" @click="filterCards">
              Apply filter
            </Button>
          </SheetClose>

          <SheetClose as-child>
            <Button
              class="text-md"
              type="button"
              variant="outline"
              @click="clearFilters"
            >
              Clear
            </Button>
          </SheetClose>
        </SheetFooter>
      </SheetContent>
    </Sheet>

    <Button variant="outline">
      <ArrowDownUp />
      Sort
    </Button>

    <div class="h-5">
      <Separator orientation="vertical" />
    </div>
  </div>
</template>
