import request from "@/utils/request"
const mem = require("mem");
const list = [
  {
    title: '推荐',
    list: [
      {
        name: '推荐歌手',
        cat: 9999
      },
      {
        name: '入驻歌手',
        cat: 5001
      }
    ]
  }
  // {
  //   title: '华语',
  //   list: [
  //     {
  //       name: '华语男歌手',
  //       cat: 1001
  //     },
  //     {
  //       name: '华语女歌手',
  //       cat: 1002
  //     },
  //     {
  //       name: '华语组合/乐队',
  //       cat: 1003
  //     }
  //   ]
  // },
  // {
  //   title: '欧美',
  //   list: [
  //     {
  //       name: '欧美男歌手',
  //       cat: 2001
  //     },
  //     {
  //       name: '欧美女歌手',
  //       cat: 2002
  //     },
  //     {
  //       name: '欧美组合/乐队',
  //       cat: 2003
  //     }
  //   ]
  // },
  // {
  //   title: '日本',
  //   list: [
  //     {
  //       name: '日本男歌手',
  //       cat: 6001
  //     },
  //     {
  //       name: '日本女歌手',
  //       cat: 6002
  //     },
  //     {
  //       name: '日本组合/乐队',
  //       cat: 6003
  //     }
  //   ]
  // },
  // {
  //   title: '韩国',
  //   list: [
  //     {
  //       name: '韩国男歌手',
  //       cat: 7001
  //     },
  //     {
  //       name: '韩国女歌手',
  //       cat: 7002
  //     },
  //     {
  //       name: '韩国组合/乐队',
  //       cat: 7003
  //     }
  //   ]
  // },
  // {
  //   title: '其他',
  //   list: [
  //     {
  //       name: '其他男歌手',
  //       cat: 4001
  //     },
  //     {
  //       name: '其他女歌手',
  //       cat: 4002
  //     },
  //     {
  //       name: '其他组合/乐队',
  //       cat: 4003
  //     }
  //   ]
  // }
]


export function getList() {
  return list;  
}

/* 歌手分类列表 */
export const getArtistList = mem(function (data) {
  return request({
    url: '/api/sing/list/',
    withCredentials: true,
    params: {
      cat: data.cat,
      limit: data.limit ? data.limit : 20,
      offset: data.offset ? data.offset : 0,
      initial: data.initial ? data.initial : ''
    }
  })
}, {
  maxAge: 1000 * 60 * 30
})

/* 热门歌手 */
export const getTopArtists = mem(function(data) {
  return request({
    url: '/api/sing/top/',
    withCredentials: true,
    params: {
      limit: data.limit ? data.limit : 20,
      offset: data.offset ? data.offset : 0
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})

/* 获取歌手单曲,传入歌手 id, 可获得歌手部分信息和热门歌曲  */
export const getArtist = mem(function (data) {
  return request({
    url: '/api/sing/artists/',
    withCredentials: true,
    params: {
      id: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})

/* 获取歌手专辑 */
export const getArtistAlbum = mem(function (data) {
  return request({
    url: '/api/sing/artist/album/',
    withCredentials: true,
    params: {
      id: data.id,
      limit: data.limit ? data.limit : 20,
      offset: data.offset ? data.offset : 0
    }
  })
},{
  maxAge: 1000 * 60 * 60
})

/* 获取歌手描述 */
export const getArtistDesc = mem(function(data) {
  return request({
    url: '/api/artist/desc',
    withCredentials: true,
    params: {
      id: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})

/* 获取歌手MV */
export const getArtistMv = mem(function (data) {
  return request({
    url: '/api/artist/mv',
    withCredentials: true,
    params: {
      id: data
    }
  })
}, {
  maxAge: 1000 * 60 * 60
})
