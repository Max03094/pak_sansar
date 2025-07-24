<!-- src/components/NotificationForm.vue -->
<template>
  <v-form>
    <v-textarea v-model="template" label="Message Template"></v-textarea>
    <v-checkbox label="SMS" v-model="methods.sms"></v-checkbox>
    <v-checkbox label="Telegram" v-model="methods.telegram"></v-checkbox>
    <v-btn @click="emit('send', { template, methods })">Send</v-btn>
  </v-form>
</template>

<script setup>
import { ref } from 'vue';
const template = ref('');
const methods = ref({ sms: false, telegram: false });
const emit = defineEmits(['send']);
</script>