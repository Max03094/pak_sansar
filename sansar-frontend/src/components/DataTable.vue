<!-- src/components/DataTable.vue -->
<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :loading="loading"
    :search="search"
    v-model:options="options"
    :server-items-length="totalItems"
    @update:options="fetchData"
  >
    <template v-slot:top>
      <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify"></v-text-field>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-btn v-if="showAccept" @click="$emit('accept', item.id)">Accept</v-btn>
      <v-btn v-if="showReady" @click="$emit('ready', item.id)">Ready</v-btn>
    </template>
  </v-data-table>
</template>

<script setup>
import { ref, watch } from 'vue';
defineProps({
  headers: Array,
  items: Array,
  loading: Boolean,
  showAccept: Boolean,
  showReady: Boolean,
  totalItems: Number
});
const emit = defineEmits(['accept', 'ready', 'update:options']);
const search = ref('');
const options = ref({ page: 1, itemsPerPage: 10 });

watch(options, () => emit('update:options', options.value));
</script>