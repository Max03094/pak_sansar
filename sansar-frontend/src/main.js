// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './stores';
import vuetify from './plugins/vuetify';
import i18n from './i18n';
import './assets/main.css';

const app = createApp(App);
app.use(router);
app.use(store);
app.use(vuetify);
app.use(i18n);
app.mount('#app');