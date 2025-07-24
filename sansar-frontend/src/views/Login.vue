<!-- src/views/Login.vue -->
<template>
  <v-container>
    <v-form>
      <v-text-field label="Username" v-model="username"></v-text-field>
      <v-text-field label="Password" type="password" v-model="password"></v-text-field>
      <v-text-field label="2FA Code" v-model="twoFaCode"></v-text-field>
      <v-btn @click="login">Login</v-btn>
    </v-form>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { connect } from '@/services/ws';

const store = useStore();
const router = useRouter();
const username = ref('');
const password = ref('');
const twoFaCode = ref('');

async function login() {
  await store.dispatch('user/login', { username: username.value, password: password.value, twoFaCode: twoFaCode.value });
  connect(store.state.user.id);
  router.push('/');
}
</script>