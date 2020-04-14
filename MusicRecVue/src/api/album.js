import request from "@/utils/request"
const mem = require("mem");
/* 新碟上架 */
export const getTopAlbum = mem(function (data) {
  return request({
    url: '/api/top/album',
    withCredentials: true,
    params: {
      limit: 20,
      offset: data.offset ? data.offset : 0
    }
  })
},{
  maxAge: 1000 * 60
})

/* 最新专辑 */
export const getAlbumNewest = mem(function () {
  return request({
    url: '/api/album/newest',
    withCredentials: true
  })
}, {
  maxAge: 1000 * 60
})

/* 获取专辑详情 */
export const getAlbum = mem(function (data) {
  return request({
    url: '/api/album',
    withCredentials: true,
    params: {
      id: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})