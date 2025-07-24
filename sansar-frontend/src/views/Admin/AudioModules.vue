<!-- src/views/Admin/AudioModules.vue -->
<template>
  <v-container>
    <DataTable :items="audioModules" :headers="headers" />
    <CrudForm :fields="fields" @save="saveAudioModule" />
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import CrudForm from '@/components/CrudForm.vue';

const store = useStore();
const audioModules = computed(() => store.state.admin.audioModules);
const headers = [
  { title: 'ID', key: 'id' },
  { title: 'IP', key: 'ip' },
  { title: 'Office', key: 'office_name' }
];
const fields = [
  { label: 'IP', key: 'ip', type: 'text' },
  { label: 'Office', key: 'office_id', type: 'select', items: computed(() => store.state.admin.offices.map(o => ({ value: o.id, text: o.name }))) }
];

function saveAudioModule(data) {
  store.dispatch('admin/saveAudioModule', data);
}
</script>