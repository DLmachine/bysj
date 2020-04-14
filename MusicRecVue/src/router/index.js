import Vue from 'vue'
import VueRouter  from 'vue-router'
Vue.use(VueRouter)
import Layout from "@/components/layout.vue"
export default new VueRouter ({
  routes: [
    {
      path: '/',
      redirect: '/home',
      component: Layout,
      children: [
        {
          path: 'home',
          name: 'home',
          component: () => import('@/views/home/index')
        },
        {
          path: 'ranking-list',
          name: 'ranking-list',
          component: () => import('@/views/rankingList/index')
        },
        {
          path: 'playlist',
          name: 'playlist',
          component: () => import('@/views/playlist/index')
        },
        {
          path: 'dj-radios',
          name: "dj-radios",
          component: () => import('@/views/dj/index')
        },
        {
          path: 'new-album',
          name: 'new-album',
          component: () => import('@/views/newAlbum/index')
        },
        {
          path: 'artist',
          name: 'artist',
          component: () => import('@/views/artist/index')
        },
        {
          path: '/my',
          name: 'my',
          component: () => import('@/views/myMusic/index'),
          children: [
            {
              path: 'daily-recommend',
              name: 'daily-recommend',
              component: () => import("@/views/myMusic/components/dailyRecommend")
            },
            {
              path: 'daily-playlist',
              name: 'daily-playlist',
              component: () => import("@/views/myMusic/components/dailyPlaylist")
            }
          ]
        },
        {
          path: '/album-detail',
          name: 'album-detail',
          component: () => import('@/views/albumDetail/index')
        },
        {
          path: '/playlist-detail',
          name: 'playlist-detail',
          component: () => import('@/views/playListDetail/index')
        },
        {
          path: '/artist-detail',
          name: 'artist-detail',
          component: () => import('@/views/artistDetail/index')
        },
        {
          path: '/mv-detail',
          name: 'mv-detail',
          component: () => import('@/views/mvDetail/index')
        },
        {
          path: '/ranking-detail',
          name: 'ranking-detail',
          component: () => import('@/views/rankingDetail/index')
        },
        {
          path: '/dj-detail',
          name: 'dj-detail',
          component: () => import('@/views/djDetail/index')
        },
        {
          path: '/search-detail',
          name: 'search-detail',
          component: () => import('@/views/searchDetail/index')
        },
        {
          path: '/song-detail',
          name: 'song-detail',
          component: () => import('@/views/songDetail/index')
        },
        {
          path: '/404',
          name: '404',
          component: () => import('@/views/errorPage')
        },
        {
          path: '/copyright',
          name: 'copyright',
          component: () => import('@/views/copyright')
        }
      ]
    },
    {
      path: '*',
      redirect: '/404',
      component: () => import('@/views/errorPage')
    }
  ],
  scrollBehavior: () => ({
    y: 0
  })
})
