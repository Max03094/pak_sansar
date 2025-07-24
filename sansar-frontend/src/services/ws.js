// src/services/ws.js (extended)
import store from '@/stores';

let ws;
export function connect(userId) {
  ws = new WebSocket(`ws://backend-url/ws/${userId}`);
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.type === 'new_alert') store.commit('alerts/setActive', [...store.state.alerts.active, data.alert]);
    if (data.type === 'status_change') store.commit('alerts/updateAlert', data.alert);
    if (data.type === 'skud_event') store.commit('skud/updateRequest', data.request);
  };
}
export function disconnect() { ws?.close(); }