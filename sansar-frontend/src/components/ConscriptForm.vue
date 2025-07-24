<!-- src/components/ConscriptForm.vue -->
<template>
  <v-form>
    <v-text-field label="IIN" v-model="iin"></v-text-field>
    <v-text-field label="FIO" v-model="fio"></v-text-field>
    <v-select label="Status" :items="statuses" v-model="status"></v-select>
    <v-btn @click="save">Save</v-btn>
  </v-form>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const iin = ref('');
const fio = ref('');
const status = ref('');
const statuses = ['Прибыл', 'Убыл'];

function save() {
  store.dispatch('skud/saveConscript', { iin: iin.value, fio: fio.value, status: status.value });
}
</script>