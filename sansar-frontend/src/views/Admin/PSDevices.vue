<!-- src/views/Admin/PSDevices.vue -->
<template>
  <v-container>
    <DataTable :items="psDevices" :headers="headers" />
    <CrudForm :fields="fields" @save="savePSDevice" />
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import CrudForm from '@/components/CrudForm.vue';

const store = useStore();
const psDevices = computed(() => store.state.admin.psDevices);
const headers = [
  { title: 'ID', key: 'id' },
  { title: 'Type', key: 'type' },
  { title: 'IP', key: 'ip' },
  { title: 'Office', key: 'office_name' }
];
const fields = [
  { label: 'Type', key: 'type', type: 'select', items: ['Sensor', 'Alarm'] },
  { label: 'IP', key: 'ip', type: 'text' },
  { label: 'Office', key: 'office_id', type: 'select', items: computed(() => store.state.admin.offices.map(o => ({ value: o.id, text: o.name }))) }
];

function savePSDevice(data) {
  store.dispatch('admin/savePSDevice', data);
}
</script>