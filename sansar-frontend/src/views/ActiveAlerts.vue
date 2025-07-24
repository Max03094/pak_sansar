<template>
  <v-container>
    <DataTable :items="activeAlerts" :headers="headers" :loading="loading" @accept="handleAccept" @ready="handleReady" />
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
const store = useStore();
const activeAlerts = computed(() => store.state.alerts.active);
const loading = ref(false);
const headers = [ /* columns */ ];

onMounted(() => store.dispatch('alerts/fetchActive'));
function handleAccept(id) { store.dispatch('alerts/accept', id); }
</script>