import request from '@/utils/request'
const mem = require("mem");
/* banner */
export const getBanner =  mem(function() {
  return request({
    url: '/api/index/banner/',
    withCredentials: true
  }) 
}, {
  maxAge: 1000 * 60 * 60
})
/* 推荐mv */
export const getPersonalizedMv = mem(function () {
  return request({
    url: '/api/index/personalized/mv/',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 推荐歌单 */
export const getPersonalized =  mem(function () {
  return request({
    url: '/api/index/personalized/',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 推荐新音乐 */
export const getPersonalizedNewSong = mem(function () {
  return request({
    url: '/api/index/personalized/newsong/',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 推荐电台 */
export const getPersonalizedDJProgram = mem(function () {
  return request({
    url: '/api/index/personalized/djprogram/',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 独家放送 */
export const getPersonalizedPrivateContent = mem(function () {
  return request({
    url: '/api/personalized/privatecontent',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
