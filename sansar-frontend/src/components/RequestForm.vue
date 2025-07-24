<!-- src/components/RequestForm.vue -->
<template>
  <v-form>
    <v-text-field label="IIN" v-model="iin" @input="fetchFIO"></v-text-field>
    <v-text-field label="FIO" v-model="fio" readonly></v-text-field>
    <v-select label="Type" :items="types" v-model="type"></v-select>
    <v-textarea label="Comment" v-model="comment"></v-textarea>
    <v-select label="Escort" :items="escorts" v-model="escort" v-if="isChief"></v-select>
    <v-btn @click="saveRequest">Save</v-btn>
    <v-btn @click="approveRequest" v-if="isChief">Approve</v-btn>
  </v-form>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const iin = ref('');
const fio = ref('');
const type = ref('');
const comment = ref('');
const escort = ref('');
const types = ['Medical', 'Other'];
const escorts = computed(() => store.state.skud.escorts);
const isChief = computed(() => store.getters['user/isChief']);

async function fetchFIO() {
  if (iin.value.length === 12) {
    const res = await store.dispatch('skud/getConscript', iin.value);
    fio.value = res.fio;
  }
}

function saveRequest() {
  store.dispatch('skud/saveRequest', { iin: iin.value, type: type.value, comment: comment.value });
}

function approveRequest() {
  store.dispatch('skud/approveRequest', { iin: iin.value, escort: escort.value });
}
</script>