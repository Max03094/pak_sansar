<!-- src/views/SKUDOffices.vue -->
<template>
  <v-container>
    <DataTable :items="logs" :headers="headers" :loading="loading" />
    <v-form>
      <v-file-input label="Photo" v-model="photo"></v-file-input>
      <v-text-field label="FIO" v-model="fio"></v-text-field>
      <v-btn @click="addFace">Add Face</v-btn>
    </v-form>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';

const store = useStore();
const logs = computed(() => store.state.skud.logs);
const loading = ref(false);
const photo = ref(null);
const fio = ref('');
const headers = [{ title: 'Date', key: 'date' }, { title: 'FIO', key: 'fio' }];

function addFace() {
  // Convert photo to base64
  const reader = new FileReader();
  reader.onload = () => store.dispatch('skud/addFace', { photo: reader.result, fio: fio.value });
  reader.readAsDataURL(photo.value[0]);
}
</script>