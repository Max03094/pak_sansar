// src/stores/admin.js (further extended)
export default {
  state: { offices: [], employees: [], permissions: {} },
  mutations: {
    setOffices(state, offices) { state.offices = offices; },
    setEmployees(state, employees) { state.employees = employees; },
    setPermissions(state, permissions) { state.permissions = permissions; },
    setPSDevices(state, devices) { state.psDevices = devices; },
    setTerminals(state, terminals) { state.terminals = terminals; },
    setPCs(state, pcs) { state.pcs = pcs; },
    setAudioModules(state, modules) { state.audioModules = modules; },
    setCameras(state, cameras) { state.cameras = cameras; }
  },
  actions: {
    async fetchOffices({ commit }) {
      const res = await api.get('/military-offices');
      commit('setOffices', res.data);
    },
    async saveOffice({ commit }, payload) {
      const res = await api.post('/military-offices', payload);
      commit('setOffices', [...state.offices, res.data]);
    },
    async fetchEmployees({ commit }) {
      const res = await api.get('/employees');
      commit('setEmployees', res.data);
    },
    async saveEmployee({ commit }, payload) {
      const res = await api.post('/employees', payload);
      commit('setEmployees', [...state.employees, res.data]);
    },
    async fetchPermissions({ commit }) {
      const res = await api.get('/roles');
      commit('setPermissions', res.data);
    },
    async savePermissions({ commit }, payload) {
      await api.post('/roles', payload);
      commit('setPermissions', payload);
    },
    async fetchPSDevices({ commit }) {
        const res = await api.get('/devices?type=ps');
        commit('setPSDevices', res.data);
    },
    async savePSDevice({ commit }, payload) {
        const res = await api.post('/devices', { ...payload, type: 'ps' });
        commit('setPSDevices', [...state.psDevices, res.data]);
    },
    async fetchTerminals({ commit }) {
        const res = await api.get('/devices?type=terminal');
        commit('setTerminals', res.data);
    },
    async saveTerminal({ commit }, payload) {
        const res = await api.post('/devices', { ...payload, type: 'terminal' });
        commit('setTerminals', [...state.terminals, res.data]);
    },
    async fetchPCs({ commit }) {
        const res = await api.get('/devices?type=pc');
        commit('setPCs', res.data);
    },
    async savePC({ commit }, payload) {
        const res = await api.post('/devices', { ...payload, type: 'pc' });
        commit('setPCs', [...state.pcs, res.data]);
    },
    async fetchAudioModules({ commit }) {
        const res = await api.get('/devices?type=audio');
        commit('setAudioModules', res.data);
    },
    async saveAudioModule({ commit }, payload) {
        const res = await api.post('/devices', { ...payload, type: 'audio' });
        commit('setAudioModules', [...state.audioModules, res.data]);
    },
    async fetchCameras({ commit }) {
        const res = await api.get('/devices?type=camera');
        commit('setCameras', res.data);
    },
    async saveCamera({ commit }, payload) {
        const res = await api.post('/devices', { ...payload, type: 'camera' });
        commit('setCameras', [...state.cameras, res.data]);
    }
  }
};