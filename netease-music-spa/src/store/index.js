import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import playlist from './modules/playlist'
import getters from './getters'
Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    user,
    playlist
  },
  getters
})

export default store
