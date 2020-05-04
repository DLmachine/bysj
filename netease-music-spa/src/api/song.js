import request from "@/utils/request.js";
const mem = require("mem");
/* 获取歌曲URL */
export function getSongUrl(data) {
  return request({
    url: '/api/song/url/',
    withCredentials: true,
    params: {
      id: data
    }
  })
}
/* 获取歌词 */
export const getLyric = mem(function(data) {
  return request({
    url: '/api/song/lyric/',
    withCredentials: true,
    params: {
      id: data
    }
  })
},{
  maxAge: 1000 * 60 * 60
})
/* 音乐是否可用 */
export function checkMusic(data) {
  return request({
    url: '/api/song/check/',
    withCredentials: true,
    params: {
      id: data
    }
  })
}
/* 歌曲评论 */
export function getCommentMusic(data) {
  return request({
    url: '/api/song/comment/',
    withCredentials: true,
    params: {
      id: data,
      limit: 50
    }
  })
}
/* 获取每日推荐歌曲(需要登录) */
export const getRecommendSongs = mem(function () {
  return request({
    url: '/api/index/recmusic/',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 获取相似歌曲 */
export const getSimilarSong = mem(function(data) {
  return request({
    url: '/api/song/sim/',
    withCredentials: true,
    params: {
      id: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 获取歌曲详情 */
export const getSongDetail = mem(function(data) {
  return request({
    url: '/api/song/detail/',
    withCredentials: true,
    params: {
      ids: data
    }
  })
},{
  maxAge: 1000 * 60 * 60
})
