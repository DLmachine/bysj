import request from "@/utils/request"
const mem = require("mem");
/* 手机密码登录 */
export function loginCellphone(data) {
  return request({
    url: '/api/index/login/',
    withCredentials: true,
    params: {
      phone: data.phone,
      password: data.password
    }
  })
}
/* 发送验证码 */
export function CaptchaSent(data){
  return request({
    url: '/api/captcha/sent',
    withCredentials: true,
    params: {
      phone: data
    }
  })
}
/* 验证验证码 */
export function CaptchaVerify(data){
  return request({
    url: '/api/captcha/verify',
    withCredentials: true,
    params: {
      phone: data.phone,
      captcha: data.captcha
    }
  })
}
/* 刷新登录状态 */
export function loginRefresh() {
  return request({
    url: '/api/login/refresh',
    withCredentials: true
  })
}
/* 登出 */
export function logout() {
  return request({
    url: '/api/index/logout/',
    withCredentials: true
  })
}
/* 登录状态 */
export function loginStatus() {
  return request({
    url: '/api/index/status/',
    withCredentials: true
  })
}
/* 获取用户详情 */
export function userDetail(data) {
  return request({
    url: '/api/user/detail',
    withCredentials: true,
    params: {
      uid: data.uid
    }
  })
}
/* 获取用户信息 , 歌单，收藏，mv, dj 数量 */
export function getUserSubCount(data) {
  return request({
    url: '/api/user/subcount',
    withCredentials: true,
  })
}
/* 获取用户歌单 */
export const getUserPlaylist = mem(function(data) {
  return request({
    url: '/api/user/playlist/',
    withCredentials: true,
    params: {
      uid: data
    }
  })
}, {
  maxAge: 1000 * 60 * 2
})
/* 获取用户播放记录 */
export function getUserRecord(data) {
  return request({
    url: '/api/user/record',
    withCredentials: true,
    params: {
      uid: data.uid,
      type: data.type
    }
  })
}
