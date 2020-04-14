import request from "@/utils/request"

/* 搜索建议 */
export function searchSuggest(data) {
  return request({
    url: '/api/search/suggest',
    withCredentials: true,
    params: {
      keywords: data
    }
  })
}

/* 搜索多重匹配 */
export function searchMultimatch(data) {
  return request({
    url: '/api/search/multimatch',
    withCredentials: true,
    params: {
      keywords: data
    }
  })
}

/* 搜索 */
/*  type: 搜索类型；默认为 1 即单曲 , 取值意义 : 1: 单曲, 10: 专辑, 
    100: 歌手, 1000: 歌单, 1002: 用户, 1004: MV, 1006: 歌词, 
    1009: 电台, 1014: 视频, 1018:综合
*/
export function search(data) {
  return request({
    url: '/api/search',
    withCredentials: true,
    params: {
      keywords: data.keywords,
      limit: 100,
      offset: data.offset ? data.offset : 0,
      type: data.type ? data.type : 1018
    }
  })
}