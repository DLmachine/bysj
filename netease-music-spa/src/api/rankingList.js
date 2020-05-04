import request from "@/utils/request.js"

const coverImgUrl= [
  {
    url:
      "http://p2.music.126.net/N2HO5xfYEqyQ8q6oxCw8IQ==/18713687906568048.jpg",
    name: "云音乐新歌榜"
  },
  {
    url:
      "http://p1.music.126.net/GhhuF6Ep5Tq9IEvLsyCN7w==/18708190348409091.jpg",
    name: "云音乐热歌榜"
  },
  {
    url:
      "http://p2.music.126.net/sBzD11nforcuh1jdLSgX7g==/18740076185638788.jpg",
    name: "网易原创歌曲榜"
  },
  {
    url:
      "http://p2.music.126.net/DrRIg6CrgDfVLEph9SNh7w==/18696095720518497.jpg",
    name: "云音乐飙升榜"
  },
  {
    url:
      "http://p2.music.126.net/8-GBrukQ3BHhs4CmK6qE4w==/109951163424197392.jpg",
    name: "云音乐国电榜"
  },
  {
    url:
      "http://p2.music.126.net/VQOMRRix9_omZbg4t-pVpw==/18930291695438269.jpg",
    name: "UK排行榜周榜"
  },
  {
    url:
      "http://p1.music.126.net/EBRqPmY8k8qyVHyF8AyjdQ==/18641120139148117.jpg",
    name: "美国Billboard排行榜"
  },
  {
    url:
      "http://p1.music.126.net/H4Y7jxd_zwygcAmPMfwJnQ==/19174383276805159.jpg",
    name: "KTV唛榜"
  },
  {
    url:
      "http://p2.music.126.net/WTpbsVfxeB6qDs_3_rnQtg==/109951163601178881.jpg",
    name: "iTunes榜Top100"
  },
  {
    url:
      "http://p1.music.126.net/54vZEZ-fCudWZm6GH7I55w==/19187577416338508.jpg",
    name: "Hit FM Top榜"
  },
  {
    url: "http://p1.music.126.net/Rgqbqsf4b3gNOzZKxOMxuw==/19029247741938160.jpg",
    name: "日本Oricon周榜"
  },
  {
    url: "http://p2.music.126.net/9YSGHPRdVazKSiNGl3uwpg==/5920870115713082.jpg",
    name: "韩国Melon排行榜周榜"
  },
  {
    url: "http://p2.music.126.net/tSl2BF3dZi4cLMD70_fYLw==/5739450697092147.jpg",
    name: "韩国Mnet排行榜周榜"
  },
  {
    url: "http://p2.music.126.net/v_cgiZ305WeM4GJiGIOu7Q==/7815328650414104.jpg",
    name: "韩国Melon原声周榜"
  },
  {
    url: "http://p1.music.126.net/JPh-zekmt0sW2Z3TZMsGzA==/18967675090783713.jpg",
    name: "中国TOP排行榜（港台榜）"
  },
  {
    url: "http://p1.music.126.net/2klOtThpDQ0CMhOy5AOzSg==/18878614648932971.jpg",
    name: "中国TOP排行榜（内地榜）"
  },
  {
    url: "http://p2.music.126.net/YQsr07nkdkOyZrlAkf0SHA==/18976471183805915.jpg",
    name: "香港电台中文歌曲龙虎榜"
  },
  {
    url: "http://p1.music.126.net/N2whh2Prf0l8QHmCpShrcQ==/19140298416347251.jpg",
    name: "华语金曲榜"
  },
  {
    url: "http://p2.music.126.net/4-m7p_OuKGrgiqPs_7yjng==/109951163573205847.jpg",
    name: "中国嘻哈榜"
  },
  {
    url: "http://p2.music.126.net/6O0ZEnO-I_RADBylVypprg==/109951162873641556.jpg",
    name: "法国 NRJ Vos Hits 周榜"
  },
  {
    url: "http://p1.music.126.net/wqi4TF4ILiTUUL5T7zhwsQ==/18646617697286899.jpg",
    name: "台湾Hito排行榜"
  },
  {
    url: "http://p2.music.126.net/A61n94BjWAb-ql4xpwpYcg==/18613632348448741.jpg",
    name: "Beatport全球电子舞曲榜"
  },
  {
    url: "http://p1.music.126.net/vttjtRjL75Q4DEnjRsO8-A==/18752170813539664.jpg",
    name: "云音乐ACG音乐榜"
  },
  {
    url: "http://p1.music.126.net/TuGxihwbiPmoHoFGvIuu_w==/109951163781770038.jpg",
    name: "江小白YOLO云音乐说唱榜"
  }
]

/* 返回coverImgUrl */
export function getCoverImgUrl(){
  return coverImgUrl
}

/* 根据idx 获取排行榜信息 */
export function getRankingList(data) {
  return request({
    url: '/api/top/list',
    withCredentials: true,
    params: {
      idx: data
    }
  })
}