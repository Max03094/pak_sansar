import { createRouter, createWebHistory } from 'vue-router';
import store from '@/stores';

const routes = [
  { path: '/login', component: () => import('@/views/Login.vue') },
  { path: '/', component: () => import('@/views/Dashboard.vue'), meta: { requiresAuth: true } },
  { path: '/active-alerts', component: () => import('@/views/ActiveAlerts.vue'), meta: { requiresAuth: true } },
  { path: '/alert-history', component: () => import('@/views/AlertHistory.vue'), meta: { requiresAuth: true } },
  { path: '/personnel-notification', component: () => import('@/views/PersonnelNotification.vue'), meta: { requiresAuth: true, roles: ['admin', 'operator'] } },
  { path: '/video-surveillance', component: () => import('@/views/VideoSurveillance.vue'), meta: { requiresAuth: true } },
  { path: '/device-status', component: () => import('@/views/DeviceStatus.vue'), meta: { requiresAuth: true } },
  { path: '/skud-offices', component: () => import('@/views/SKUDOffices.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/skud-collection', component: () => import('@/views/SKUDCollection.vue'), meta: { requiresAuth: true, roles: ['admin', 'doctor'] } },
  { path: '/audio-alert', component: () => import('@/views/AudioAlert.vue'), meta: { requiresAuth: true, roles: ['admin', 'operator'] } },
  { path: '/admin/offices', component: () => import('@/views/Admin/Offices.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/employees', component: () => import('@/views/Admin/Employees.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/roles', component: () => import('@/views/Admin/RolesPermissions.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/cameras', component: () => import('@/views/Admin/Cameras.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/ps-devices', component: () => import('@/views/Admin/PSDevices.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/terminals', component: () => import('@/views/Admin/Terminals.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/pcs', component: () => import('@/views/Admin/PCs.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/audio-modules', component: () => import('@/views/Admin/AudioModules.vue'), meta: { requiresAuth: true, roles: ['admin'] } },
  { path: '/admin/system-monitor', component: () => import('@/views/Admin/SystemMonitor.vue'), meta: { requiresAuth: true, roles: ['admin'] } }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !store.getters.isAuthenticated) return next('/login');
  if (to.meta.roles && !to.meta.roles.includes(store.state.user.role)) return next('/');
  next();
});

export default router;