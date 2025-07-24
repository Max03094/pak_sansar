<!-- src/views/Admin/PCs.vue -->
<template>
  <v-container>
    <DataTable :items="pcs" :headers="headers" />
    <CrudForm :fields="fields" @save="savePC" />
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import CrudForm from '@/components/CrudForm.vue';

const store = useStore();
const pcs = computed(() => store.state.admin.pcs);
const headers = [
  { title: 'ID', key: 'id' },
  { title: 'IP', key: 'ip' },
  { title: 'Office', key: 'office_name' }
];
const fields = [
  { label: 'IP', key: 'ip', type: 'text' },
  { label: 'Office', key: 'office_id', type: 'select', items: computed(() => store.state.admin.offices.map(o => ({ value: o.id, text: o.name }))) }
];

function savePC(data) {
  store.dispatch('admin/savePC', data);
}
</script>