<!-- src/views/Admin/Offices.vue -->
<template>
  <v-container>
    <DataTable :items="offices" :headers="headers" />
    <CrudForm :fields="fields" @save="saveOffice" />
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import CrudForm from '@/components/CrudForm.vue';

const store = useStore();
const offices = computed(() => store.state.admin.offices);
const headers = [
  { title: 'ID', key: 'id' },
  { title: 'District', key: 'district' },
  { title: 'City', key: 'city' },
  { title: 'Name', key: 'name' }
];
const fields = [
  { label: 'District', key: 'district', type: 'select', items: ['District1', 'District2'] },
  { label: 'City', key: 'city', type: 'select', items: ['City1', 'City2'] },
  { label: 'Name', key: 'name', type: 'text' }
];

function saveOffice(data) {
  store.dispatch('admin/saveOffice', data);
}
</script>