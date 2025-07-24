<!-- src/views/Admin/Employees.vue -->
<template>
  <v-container>
    <DataTable :items="employees" :headers="headers" />
    <CrudForm :fields="fields" @save="saveEmployee" />
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import CrudForm from '@/components/CrudForm.vue';

const store = useStore();
const employees = computed(() => store.state.admin.employees);
const headers = [
  { title: 'FIO', key: 'fio' },
  { title: 'Rank', key: 'rank' },
  { title: 'Office', key: 'office_name' },
  { title: 'Phone', key: 'phone' }
];
const fields = [
  { label: 'FIO', key: 'fio', type: 'text' },
  { label: 'Rank', key: 'rank', type: 'select', items: ['Officer', 'Soldier'] },
  { label: 'Office', key: 'office_id', type: 'select', items: computed(() => store.state.admin.offices.map(o => ({ value: o.id, text: o.name }))) },
  { label: 'Phone', key: 'phone', type: 'text' }
];

function saveEmployee(data) {
  store.dispatch('admin/saveEmployee', data);
}
</script>