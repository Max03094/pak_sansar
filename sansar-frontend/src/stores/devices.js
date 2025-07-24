// src/stores/devices.js
import api from '@/services/api';

export default {
  state: { tree: [] },
  mutations: { setTree(state, tree) { state.tree = tree; } },
  actions: {
    async fetchTree({ commit }) {
      const res = await api.get('/devices/status');
      commit('setTree', res.data); // Assume tree structure
    }
  }
};