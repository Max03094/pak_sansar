// src/stores/alerts.js
import api from '@/services/api';

export default {
  state: {
    active: [],
    history: []
  },
  mutations: {
    setActive(state, alerts) { state.active = alerts; },
    setHistory(state, alerts) { state.history = alerts; },
    updateAlert(state, updatedAlert) {
      const index = state.active.findIndex(a => a.id === updatedAlert.id);
      if (index !== -1) state.active.splice(index, 1, updatedAlert);
    }
  },
  actions: {
    async fetchActive({ commit }) {
      const res = await api.get('/alerts?status=active');
      commit('setActive', res.data);
    },
    async fetchHistory({ commit }, filters) {
      const res = await api.get('/alerts?status=history', { params: filters });
      commit('setHistory', res.data);
    },
    async accept({ commit }, id) {
      const res = await api.put(`/alerts/${id}`, { status: 'accepted' });
      commit('updateAlert', res.data);
    },
    async ready({ commit }, id) {
      const res = await api.put(`/alerts/${id}`, { status: 'ready' });
      commit('updateAlert', res.data);
    }
  }
};