// src/stores/video.js
import api from '@/services/api';

export default {
  state: {
    offices: [] // Tree structure
  },
  mutations: {
    setOffices(state, offices) { state.offices = offices; }
  },
  actions: {
    async fetchOffices({ commit }) {
      const res = await api.get('/military-offices'); // Adapt for tree
      commit('setOffices', res.data);
    },
    async fetchStream(_, deviceId) {
      const res = await api.get(`/video/stream/${deviceId}`);
      return res.data.url;
    }
  }
};