import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
// import '@/styles/index.less'
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
// 引入echarts
import * as echarts from 'echarts'
import 'echarts-wordcloud';
Vue.prototype.$echarts = echarts;

Vue.prototype.$axios = axios;    //全局注册，使用方法为:this.$axios

Vue.use(ElementUI);
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
