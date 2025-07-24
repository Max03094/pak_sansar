<!-- src/views/Admin/RolesPermissions.vue -->
<template>
  <v-container>
    <v-textarea v-model="permissionsJson" label="Permissions JSON"></v-textarea>
    <v-btn @click="savePermissions">Save</v-btn>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const permissionsJson = ref(JSON.stringify(computed(() => store.state.admin.permissions).value, null, 2));

function savePermissions() {
  store.dispatch('admin/savePermissions', JSON.parse(permissionsJson.value));
}
</script>