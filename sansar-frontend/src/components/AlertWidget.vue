<!-- src/components/AlertWidget.vue -->
<template>
  <v-card>
    <v-card-title>Active Alerts</v-card-title>
    <v-card-text>{{ count }}</v-card-text>
  </v-card>
</template>

<script setup>
defineProps({ count: Number });
</script>