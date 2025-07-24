<!-- src/views/DeviceStatus.vue -->
<template>
  <v-container>
    <TreeView :items="devicesTree" />
  </v-container>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import TreeView from '@/components/TreeView.vue';

const store = useStore();
const devicesTree = computed(() => store.state.devices.tree);

onMounted(() => store.dispatch('devices/fetchTree'));
</script>