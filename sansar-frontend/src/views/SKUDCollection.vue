<!-- src/views/SKUDCollection.vue -->
<template>
  <v-tabs v-model="tab">
    <v-tab value="conscripts">Conscripts</v-tab>
    <v-tab value="requests">Requests</v-tab>
  </v-tabs>
  <v-window v-model="tab">
    <v-window-item value="conscripts">
      <DataTable :items="conscripts" :headers="conscriptHeaders" />
      <ConscriptForm />
    </v-window-item>
    <v-window-item value="requests">
      <DataTable :items="requests" :headers="requestHeaders" />
      <RequestForm />
    </v-window-item>
  </v-window>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';
import ConscriptForm from '@/components/ConscriptForm.vue';
import RequestForm from '@/components/RequestForm.vue';

const tab = ref('conscripts');
const store = useStore();
const conscripts = computed(() => store.state.skud.conscripts);
const requests = computed(() => store.state.skud.requests);
const conscriptHeaders = [{ title: 'IIN', key: 'iin' }, { title: 'FIO', key: 'fio' }];
const requestHeaders = [{ title: 'IIN', key: 'iin' }, { title: 'Type', key: 'type' }];
</script>