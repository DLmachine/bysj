import Vue from 'vue'
import Vuex from 'vuex'
import playlist from './modules/playlist'
import rankData from './modules/rankData'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({

  modules: {
    playlist,
    rankData
  },
  strict: debug,
  plugins:  []
})
