<template>
  <v-container>
    <v-row>
      <v-col>
        <v-text-field v-model="filters.dateFrom" label="From Date" type="date"></v-text-field>
      </v-col>
      <v-col>
        <v-text-field v-model="filters.dateTo" label="To Date" type="date"></v-text-field>
      </v-col>
      <v-col>
        <v-btn @click="fetchHistory">Filter</v-btn>
        <v-btn @click="exportCSV">Export CSV</v-btn>
      </v-col>
    </v-row>
    <DataTable :items="historyAlerts" :headers="headers" :loading="loading" />
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import * as XLSX from 'xlsx';

const store = useStore();
const historyAlerts = computed(() => store.state.alerts.history);
const loading = ref(false);
const filters = ref({ dateFrom: '', dateTo: '' });
const headers = [
  { title: 'ID', key: 'id' },
  { title: 'Office', key: 'office_name' },
  { title: 'Type', key: 'type' },
  { title: 'Time', key: 'time' },
  { title: 'Total Mins', key: 'total_time' }
];

onMounted(() => fetchHistory());

async function fetchHistory() {
  loading.value = true;
  await store.dispatch('alerts/fetchHistory', filters.value);
  loading.value = false;
}

function exportCSV() {
  const ws = XLSX.utils.json_to_sheet(historyAlerts.value);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'History');
  XLSX.writeFile(wb, 'alert_history.xlsx');
}
</script>