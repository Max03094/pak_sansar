<!-- src/views/PersonnelNotification.vue -->
<template>
  <v-container>
    <v-row>
      <v-col>
        <v-select v-model="office" :items="offices" label="Office"></v-select>
      </v-col>
      <v-col>
        <v-textarea v-model="template" label="Message Template"></v-textarea>
      </v-col>
    </v-row>
    <DataTable :items="employees" :headers="headers" v-model:selected="selected" show-checkbox>
      <template v-slot:top>
        <v-checkbox label="SMS" v-model="methods.sms"></v-checkbox>
        <v-checkbox label="Telegram" v-model="methods.telegram"></v-checkbox>
        <v-btn @click="sendNotifications">Send</v-btn>
      </template>
    </DataTable>
  </v-container>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useStore } from 'vuex';
import DataTable from '@/components/DataTable.vue';

const store = useStore();
const office = ref(null);
const template = ref('');
const methods = ref({ sms: false, telegram: false });
const selected = ref([]);
const employees = computed(() => store.state.notifications.employees);
const offices = computed(() => store.state.admin.offices);
const headers = [
  { title: 'FIO', key: 'fio' },
  { title: 'Rank', key: 'rank' },
  { title: 'Phone', key: 'phone' }
];

watch(office, () => store.dispatch('notifications/fetchEmployees', office.value));

function sendNotifications() {
  store.dispatch('notifications/send', { selected: selected.value, methods: methods.value, template: template.value });
}
</script>