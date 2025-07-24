// src/stores/index.js
import { createStore } from 'vuex';
import user from './user';
import alerts from './alerts';
// Add others

export default createStore({
  modules: { user, alerts /* , ... */ }
});