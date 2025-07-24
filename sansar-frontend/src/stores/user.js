// src/stores/user.js
import api from '@/services/api';
export default {
  state: { token: null, role: null },
  getters: { isAuthenticated: state => !!state.token },
  mutations: {
    setToken(state, token) { state.token = token; },
    setRole(state, role) { state.role = role; }
  },
  actions: {
    async login({ commit }, creds) {
      const res = await api.post('/auth/login', creds);
      commit('setToken', res.token);
      commit('setRole', res.role);
    },
    logout({ commit }) { commit('setToken', null); }
  }
};