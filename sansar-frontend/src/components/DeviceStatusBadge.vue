<!-- src/components/DeviceStatusBadge.vue -->
<template>
  <v-chip :color="statusColor">{{ statusText }}</v-chip>
</template>

<script setup>
defineProps({
  status: String
});
const statusColor = computed(() => ({
  online: 'green',
  offline: 'red',
  alarm: 'yellow'
}[props.status] || 'grey'));
const statusText = computed(() => props.status || 'Unknown');
</script>