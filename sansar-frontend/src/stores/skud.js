// src/stores/skud.js (extended)
export default {
  state: {
    logs: [],
    conscripts: [],
    requests: [],
    escorts: []
  },
  mutations: {
    setLogs(state, logs) { state.logs = logs; },
    setConscripts(state, conscripts) { state.conscripts = conscripts; },
    setRequests(state, requests) { state.requests = requests; },
    setEscorts(state, escorts) { state.escorts = escorts; },
    updateRequest(state, updated) {
      const index = state.requests.findIndex(r => r.iin === updated.iin);
      if (index !== -1) state.requests.splice(index, 1, updated);
    }
  },
  actions: {
    async fetchLogs({ commit }) {
      const res = await api.get('/skud/logs');
      commit('setLogs', res.data);
    },
    async addFace(_, payload) {
      await api.post('/skud/add-face', payload);
    },
    async fetchConscripts({ commit }) {
      const res = await api.get('/conscripts');
      commit('setConscripts', res.data);
    },
    async saveConscript({ commit }, payload) {
      const res = await api.post('/conscripts', payload);
      commit('setConscripts', [...state.conscripts, res.data]);
    },
    async getConscript(_, iin) {
      const res = await api.get(`/conscripts/${iin}`);
      return res.data;
    },
    async fetchRequests({ commit }) {
      const res = await api.get('/requests');
      commit('setRequests', res.data);
    },
    async saveRequest({ commit }, payload) {
      const res = await api.post('/requests', payload);
      commit('setRequests', [...state.requests, res.data]);
    },
    async approveRequest({ commit }, payload) {
      const res = await api.post('/requests/approve', payload);
      commit('updateRequest', res.data);
    },
    async fetchEscorts({ commit }) {
      const res = await api.get('/employees?role=escort');
      commit('setEscorts', res.data);
    }
  }
};