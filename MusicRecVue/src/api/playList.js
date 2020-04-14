import request from "@/utils/request.js"
const mem = require("mem");
/*歌单分类（全部）  */
export const getPlayListCatlist = mem(function () {
  return request({
    url: '/api/playlist/catlist/',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 热门歌单分类 */
export function getPlayListHot() {
  return request({
    url: '/api/playlist/hot',
    withCredentials: true
  })
}
/*获取歌单 ( 网友精选碟 )  */
export const getPlayList = mem(function (data) {
  return request({
    url: '/api/playlist/top/',
    withCredentials: true,
    params: {
      limit: 20,
      cat: data.cat ? data.cat : '',
      offset: data.offset ? data.offset : 0
    }
  })
}, {
  maxAge: 1000 * 60 * 30
})
/* 获取精品歌单 */
export function getPlaylistHighQuality(data) {
  return request({
    url: '/api/playlist/highquality',
    withCredentials: true,
    params: {
      before: data.before? data.before : ''
    }
  })
}
/*相关歌单推荐  */
export function getRelatedPlaylist(data) {
  return request({
    url: '/api/related/playlist',
    withCredentials: true,
    params: {
      id: data
    }
  })
}
/* 获取歌单详情 */
export function getPlaylistDetail(data) {
  return request({
    url: '/api/playlist/detail/',
    withCredentials: true,
    params: {
      id: data
    }
  })
}
/* 获取每日推荐歌单(需要登录) */
export const getRecommendResource = mem(function () {
  return request({
    url: '/api/recommend/resource',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 获取相似歌单(包含这首歌的歌单) */
export const getSimilarPlaylist = mem(function(data) {
  return request({
    url: '/api/simi/playlist',
    withCredentials: true,
    params: {
      id: data
    }
  })
},{
  maxAge: 1000 * 60 * 60
})
/* 收藏、取消收藏歌单 */
export function subscribePlaylist(data) {
  return request({
    url: '/api/playlist/subscribe',
    withCredentials: true,
    params: {
      id: data.id,
      t: data.type
    }
  })
}
