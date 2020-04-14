import request from "@/utils/request"

/* 获取mv地址 */
export function getMvUrl(data) {
  return request({
    url: '/api/mv/url',
    withCredentials: true,
    params: {
      id: data
    }
  })
}

/* 获取MV详情 */
export function getMvDetail(data) {
  return request({
    url: '/api/mv/detail',
    withCredentials: true,
    params: {
      mvid: data
    }
  })
}

/* 获取mv评论 */
export function getCommentMv(data) { 
  return request({
    url: '/api/comment/mv',
    withCredentials: true,
    params: {
      id: data,
      limit: 20,
      offset: 0
    }
  })
}

/* 获取视频地址 */
export function getVideoUrl(data) {
  return request({
    url: '/api/video/url',
    withCredentials: true,
    params: {
      id: data
    }
  })
}

/* 获取视频详情 */
export function getVideoDetail(data) {
  return request({
    url: '/api/video/detail',
    withCredentials: true,
    params: {
      id: data
    }
  })
}

/* 获取视频评论 */
export function getCommentVideo(data) { 
  return request({
    url: '/api/comment/video',
    withCredentials: true,
    params: {
      id: data,
      limit: 20,
      offset: 0
    }
  })
}