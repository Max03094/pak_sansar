<!-- src/views/VideoSurveillance.vue -->
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="3">
        <TreeView :items="offices" @select="loadStream" />
      </v-col>
      <v-col cols="9">
        <VideoPlayer v-if="streamUrl" :url="streamUrl" />
        <v-badge v-if="aiDetection" color="red" content="Duty Present"></v-badge>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import TreeView from '@/components/TreeView.vue';
import VideoPlayer from '@/components/VideoPlayer.vue';

const store = useStore();
const streamUrl = ref(null);
const aiDetection = ref(false);
const offices = computed(() => store.state.video.offices);

function loadStream(deviceId) {
  store.dispatch('video/fetchStream', deviceId).then(url => {
    streamUrl.value = url;
    // Fetch AI detection status
  });
}
</script>