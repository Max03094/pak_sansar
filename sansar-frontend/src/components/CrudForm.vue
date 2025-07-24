<!-- src/components/CrudForm.vue -->
<template>
  <v-form @submit.prevent="emit('save', formData)">
    <v-text-field
      v-for="field in fields"
      :key="field.key"
      :label="field.label"
      :type="field.type === 'select' ? 'text' : field.type"
      v-model="formData[field.key]"
      :items="field.items"
      :select="field.type === 'select'"
    ></v-text-field>
    <v-btn type="submit">Save</v-btn>
  </v-form>
</template>

<script setup>
import { ref } from 'vue';
defineProps({ fields: Array });
const emit = defineEmits(['save']);
const formData = ref({});
</script>