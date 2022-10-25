import { createApp } from 'vue';
// import './cookiestore-polyfill';
import './assets/main.scss';
import App from './App.vue';

// https://github.com/niyazpk/cookie-wrapper
// eslint-disable-next-line func-names
window.Cookie = (function () {
  function set(name, value, seconds) {
    if (typeof value === 'object') {
      // eslint-disable-next-line no-param-reassign
      value = JSON.stringify(value);
    }

    const date = new Date();
    let expires = '; expires=';

    if (typeof seconds !== 'undefined') {
      date.setTime(date.getTime() + (seconds * 1000));
      expires += date.toGMTString();
    } else {
      expires = '';
    }
    document.cookie = `${name}=${encodeURIComponent(value)}${expires}; path=/`;
  }

  function get(name) {
    const nameEQ = `${name}=`;
    const ca = document.cookie.split(';');
    // eslint-disable-next-line no-plusplus
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') { c = c.substring(1, c.length); }
      try {
        if (c.indexOf(nameEQ) === 0) {
          // eslint-disable-next-line vars-on-top, no-var
          var v = decodeURIComponent(c.substring(nameEQ.length, c.length));
          return JSON.parse(v);
        }
      } catch (e) {
        // eslint-disable-next-line block-scoped-var
        return v;
      }
    }
    return null;
  }

  function clear(name) {
    set(name, '', -1);
  }

  return {
    get,
    set,
    clear,
  };
}());

createApp(App).mount('#app');
