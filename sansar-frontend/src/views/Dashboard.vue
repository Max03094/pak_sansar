<!-- src/views/Dashboard.vue -->
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        <AlertWidget :count="activeAlertCount" />
      </v-col>
      <v-col cols="4">
        <v-card>
          <v-card-title>Device Status</v-card-title>
          <v-card-text>
            <v-chip :color="deviceStatus.online ? 'green' : 'red'">{{ deviceStatus.online }} Online</v-chip>
            <v-chip color="yellow">{{ deviceStatus.alarm }} Alarms</v-chip>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card>
          <v-card-title>Response Times</v-card-title>
          <canvas id="responseChart"></canvas>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import AlertWidget from '@/components/AlertWidget.vue';
import Chart from 'chart.js/auto';

const store = useStore();
const activeAlertCount = computed(() => store.state.alerts.active.length);
const deviceStatus = computed(() => store.state.devices.status);

onMounted(async () => {
  await store.dispatch('devices/fetchStatus');
  const ctx = document.getElementById('responseChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar'], // Example
      datasets: [{ label: 'Response Time (min)', data: [5, 10, 8], borderColor: '#42A5F5' }]
    }
  });
});
</script>

```chartjs
{
  "type": "line",
  "data": {
    "labels": ["Jan", "Feb", "Mar"],
    "datasets": [{
      "label": "Response Time (min)",
      "data": [5, 10, 8],
      "borderColor": "#42A5F5",
      "backgroundColor": "rgba(66, 165, 245, 0.2)",
      "fill": true
    }]
  },
  "options": {
    "responsive": true,
    "scales": {
      "y": { "beginAtZero": true }
    }
  }
}