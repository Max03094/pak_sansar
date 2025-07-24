<!-- src/components/AudioSendForm.vue -->
<template>
  <v-form>
    <v-checkbox-group v-model="selectedOffices" :items="offices"></v-checkbox-group>
    <v-select label="Alert Type" :items="types" v-model="type"></v-select>
    <v-btn @click="emit('send', { offices: selectedOffices, type })">Send</v-btn>
  </v-form>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';
defineProps({ offices: Array, types: Array });
const selectedOffices = ref([]);
const type = ref('');
const emit = defineEmits(['send']);
</script>