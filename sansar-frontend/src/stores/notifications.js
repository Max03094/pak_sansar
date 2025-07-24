// src/stores/notifications.js
import api from '@/services/api';

export default {
  state: {
    employees: []
  },
  mutations: {
    setEmployees(state, employees) { state.employees = employees; }
  },
  actions: {
    async fetchEmployees({ commit }, office) {
      const res = await api.get('/employees', { params: { office } });
      commit('setEmployees', res.data);
    },
    async send(_, payload) {
      await api.post('/notifications', payload);
    }
  }
};