// src/stores/audio.js
import api from '@/services/api';

export default {
  state: {},
  actions: {
    async send(_, payload) {
      await api.post('/audio/send', payload);
    }
  }
};