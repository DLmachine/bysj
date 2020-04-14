import request from "@/utils/request.js"
const mem = require("mem");
/* 电台推荐 */
export const getDjRecommend = mem(function () {
  return request({
    url: '/api/dj/recommend',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 推荐节目 */
export const getProgramRecommend = mem(function () {
  return request({
    url: '/api/program/recommend',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 电台分类 */
export const getDjCateList = mem(function () {
  return request({
    url: '/api/dj/catelist',
    withCredentials: true
  })
},{
  maxAge: 1000 * 60 * 60
})
/* 电台分类推荐 */
export const getDjRecommendType = mem(function (data) {
  return request({
    url: '/api/dj/recommend/type',
    withCredentials: true,
    params: {
      type: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 今日电台推荐 */
export const getTodayDj = mem(function () {
  return request({
    url: '/api/dj/today/perfered',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 电台详情 */
export const getDjDetail = mem(function (data) {
  return request({
    url: '/api/dj/detail',
    withCredentials: true,
    params: {
      rid: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})
/* 电台节目 */
export const getDjProgram = mem(function (data) {
  return request({
    url: '/api/dj/program',
    withCredentials: true,
    params: {
      rid: data.rid,
      limit: data.limit
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})