<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';
import { SlidersHorizontal, ArrowDownUp } from 'lucide-vue-next';
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';

const types = [
  'Colorless', 'Darkness', 'Dragon', 'Fairy', 'Fighting', 'Fire',
  'Grass', 'Lightning', 'Metal', 'Psychic', 'Water',
];

const selectedType = ref<string | null>(null);

const router = useRouter();
const route = useRoute();

function syncFiltersFromURL() {
  const t = route.query.types as string | undefined;
  if (t && types.includes(t)) {
    selectedType.value = t;
  } else {
    selectedType.value = null;
  }
}

function applyFilters() {
  const query = { ...route.query };

  if (selectedType.value) {
    query.types = selectedType.value.toLowerCase();
  } else {
    delete query.types;
  }

  router.push({ path: '/cards', query });
}

function clearFilters() {
  selectedType.value = null;

  const { types, ...rest } = route.query;
  router.push({ path: '/cards', query: rest });
}

onMounted(syncFiltersFromURL);
watch(() => route.query.types, syncFiltersFromURL);

function toggleType(type: string, checked: boolean) {
  if (checked) {
    selectedType.value = type;
  } else {
    selectedType.value = null;
  }
}
</script>

<template>
  <div
    class="flex justify-start items-center w-full h-16 pt-3 px-4 bg-white dark:bg-black text-gray-800 dark:text-gray-300 shadow-md space-x-4">
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
          <SheetDescription>Use the filters below to customize the displayed cards.</SheetDescription>
        </SheetHeader>

        <div class="overflow-y-auto px-4 py-2 space-y-2 flex-1">
          <Separator />
          <label class="font-semibold text-lg">Type</label>

          <div v-for="type in types" :key="type" class="flex items-center space-x-2 pt-2">
            <input type="checkbox" :id="`type-${type}`" :value="type" :checked="selectedType === type"
              @change="e => toggleType(type, e.target.checked)" class="cursor-pointer" />
            <label :for="`type-${type}`" class="text-md font-medium leading-none cursor-pointer">
              {{ type }}
            </label>
          </div>
        </div>

        <SheetFooter class="shrink-0 px-4 pb-4 space-x-2">
          <SheetClose as-child>
            <Button class="text-md" type="button" @click="applyFilters">
              Apply filter
            </Button>
          </SheetClose>

          <SheetClose as-child class="shrink-0 px-4 pb-4 space-x-2">
            <Button class="text-md" type="button" variant="outline" @click="clearFilters">
              Clear
            </Button>
          </SheetClose>
        </SheetFooter>
      </SheetContent>
    </Sheet>

    <Button variant="outline" disabled>
      <ArrowDownUp />
      Sort
    </Button>

    <div class="h-5">
      <Separator orientation="vertical" />
    </div>
  </div>
</template>
