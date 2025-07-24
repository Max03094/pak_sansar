<!-- src/views/Admin/Cameras.vue -->
<template>
  <v-container>
    <DataTable :items="cameras" :headers="headers" />
    <CrudForm :fields="fields" @save="saveCamera" />
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import CrudForm from '@/components/CrudForm.vue';

const store = useStore();
const cameras = computed(() => store.state.admin.cameras);
const headers = [
  { title: 'ID', key: 'id' },
  { title: 'IP', key: 'ip' },
  { title: 'Login', key: 'login' },
  { title: 'Office', key: 'office_name' }
];
const fields = [
  { label: 'IP', key: 'ip', type: 'text' },
  { label: 'Login', key: 'login', type: 'text' },
  { label: 'Password', key: 'password', type: 'password' },
  { label: 'Office', key: 'office_id', type: 'select', items: computed(() => store.state.admin.offices.map(o => ({ value: o.id, text: o.name }))) }
];

function saveCamera(data) {
  store.dispatch('admin/saveCamera', data);
}
</script>