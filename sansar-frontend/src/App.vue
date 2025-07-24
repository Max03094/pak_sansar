<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>Sansar</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-select v-model="$i18n.locale" :items="['ru', 'kz']" density="compact"></v-select>
      <v-btn @click="logout">Logout</v-btn>
    </v-app-bar>
    <v-navigation-drawer app v-if="isAuthenticated">
      <v-list>
        <v-list-item v-for="item in menuItems" :key="item.title" :to="item.route">
          {{ $t(item.title) }}
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore();
const isAuthenticated = computed(() => store.getters.isAuthenticated);
const menuItems = computed(() => {
  // Filter based on role
  return [
    { title: 'dashboard', route: '/' },
    // Add others conditionally
  ];
});
function logout() {
  store.dispatch('user/logout');
}
</script>