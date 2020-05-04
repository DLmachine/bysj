import request from "@/utils/request"
 
/* 评论 

0: 歌曲

1: mv

2: 歌单

3: 专辑

4: 电台

5: 视频

6: 动态

*/
export function comment(data) {
  return request({
    url: '/api/comment',
    withCredentials: true,
    params: {
      t: 1,
      type: data.type,
      id: data.id,
      content: data.content ? data.content : '赞'
    }
  })
}