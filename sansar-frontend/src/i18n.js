// src/i18n.js
import { createI18n } from 'vue-i18n';
import ru from './locales/ru.json';
import kz from './locales/kz.json';

const i18n = createI18n({
  locale: 'ru',
  fallbackLocale: 'ru',
  messages: { ru, kz }
});

export default i18n;