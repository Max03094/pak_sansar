<!-- src/components/VideoPlayer.vue -->
<template>
  <video controls :src="url" autoplay></video>
</template>

<script setup>
defineProps({ url: String });
</script>