import router from './router'
import store from './store'
import NProgress from 'nprogress' // Progress 进度条
import 'nprogress/nprogress.css'// Progress 进度条样式
import Vue from 'vue'

const whiteList = ['/home', '/ranking-list', '/playlist', '/dj-radios', '/new-album',
  '/artist', '/album-detail', '/playlist-detail', '/artist-detail', '/mv-detail', '/ranking-detail',
  '/dj-detail', '/search-detail', '/song-detail', '/404', '/copyright']
router.beforeEach((to, from, next) => {
  NProgress.start();
  if (store.getters.loginSuccess) { //如果已登录，直接跳转
    next();
  } else {
    if (whiteList.indexOf(to.path) !== -1) { //to.path在白名单内
      next();
    } else {
      Vue.prototype.$message.warning('请先登录再体验该功能喔...')
      NProgress.done()
    }
  }
  
})

router.afterEach(() => {
  NProgress.done();
})