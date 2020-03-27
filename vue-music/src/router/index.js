import Vue from 'vue'
import Router from 'vue-router'

//导航页面
import Index from '../page/Index.vue'
import Artists from '../page/Artistslib.vue'
import Albumlib from '../page/Albumlib.vue'
import Ranklib from '../page/Ranklib.vue'
import Classifylib from '../page/Classifylib.vue'
import Radiolib from '../page/Radiolib.vue'
import MVlib from '../page/MVlib.vue'

import Play from '../page/Play.vue'
import MVDetail from '../page/MVDetail.vue'
import Singer from '../page/Singer.vue'
import RadioPage from '../page/RadioDetail.vue'
import SearchPage from '../page/SearchPage.vue'
import SongDetail from '../page/SongDetail.vue'
import Login from '../components/Login'
// import store from "../../../MusicRec-Vue/src/store";
// import router from "../../../MusicRec-Vue/src/router";

Vue.use(Router)
const router = new Router({
  mode: 'history',
  routes: [
    {
      path:'/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/artists/:id?',
      name: 'Artists',
      component: Artists,
    },
    {
      path: '/album/:id?',
      name: 'Albumlib',
      component: Albumlib
    },
    {
      path: '/rank',
      name: 'Ranklib',
      component: Ranklib
    },
    {
      path: '/classify',
      name: 'Classifylib',
      component: Classifylib
    },
    {
      path: '/radio/:id?',
      name: 'Radiolib',
      component: Radiolib
    },
    {
      path: '/radio_page/:id',
      name: 'RadioPage',
      component: RadioPage
    },
    {
      path: '/mv/:id?',
      name: 'MV',
      component: MVlib
    },
    {
      path: '/singer/:id',
      name: 'Singer',
      component: Singer
    },
    {
      path: '/song/:id',
      name: 'SongDetail',
      component: SongDetail
    },
    {
      path: '/play',
      name: 'play',
      component: Play
    },
    {
      path: '/play/song*/:id',
      name: 'songplay',
      component: Play
    },
     {
      path: '/play/album/:id',
      name: 'albumplay',
      component: Play
    },
    {
      path: '/play/mv/:id',
      name: 'mvplay',
      component: MVDetail
    },
    {
      path: '/search*',
      name: 'search',
      component: SearchPage
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.needLogin) {
    if (store.state.vuexlogin.isLogin || localStorage.getItem('username')) {
      next()
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
})

export default router
