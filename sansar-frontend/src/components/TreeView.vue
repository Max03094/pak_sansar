<!-- src/components/TreeView.vue -->
<template>
  <v-treeview :items="items" @update:selected="onSelect"></v-treeview>
</template>

<script setup>
defineProps({ items: Array });
const emit = defineEmits(['select']);
function onSelect(node) { emit('select', node.id); }
</script>