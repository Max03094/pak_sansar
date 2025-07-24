<!-- src/views/AudioAlert.vue -->
<template>
  <v-container>
    <v-checkbox-group v-model="selectedOffices" :items="offices"></v-checkbox-group>
    <v-select label="Alert Type" :items="alertTypes" v-model="alertType"></v-select>
    <v-btn @click="sendAudio">Send</v-btn>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const selectedOffices = ref([]);
const alertType = ref('');
const alertTypes = ['Warning', 'Emergency'];
const offices = computed(() => store.state.admin.offices);

function sendAudio() {
  store.dispatch('audio/send', { offices: selectedOffices.value, type: alertType.value });
}
</script>