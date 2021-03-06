import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import dataV from '@jiaminghi/data-view';
Vue.use(dataV);

// 按需引入vue-awesome图标
import Icon from 'vue-awesome/components/Icon';
import 'vue-awesome/icons/chart-bar.js';
import 'vue-awesome/icons/chart-area.js';
import 'vue-awesome/icons/chart-pie.js';
import 'vue-awesome/icons/chart-line.js';
import 'vue-awesome/icons/align-left.js';
import 'vue-awesome/icons/caret-left.js';
import 'vue-awesome/icons/caret-right.js';
import 'vue-awesome/icons/arrow-up.js';
import 'vue-awesome/icons/arrow-down.js';
import 'vue-awesome/icons/arrow-right.js';
import 'vue-awesome/icons/sort.js';
import 'vue-awesome/icons/map.js';
import 'vue-awesome/icons/laptop.js';
import 'vue-awesome/icons/sort-amount-down.js';

// 全局注册图标
Vue.component('icon', Icon);

// 适配flex
import '@/common/flexible.js';

// 引入全局css
import './assets/scss/style.scss';


// 引入echart
import echarts from 'echarts'
Vue.prototype.$echarts = echarts

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount('#app');