import { cookieStore } from 'cookie-store';
import { createApp } from 'vue';
import './assets/main.scss';
import App from './App.vue';

const isChrome = !!window.chrome;

if (!isChrome) {
  window.cookieStore = cookieStore; // polyfill for Cookie Store API, present only in chrome
}

createApp(App).mount('#app');
