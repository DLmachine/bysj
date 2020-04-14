import { getSongUrl, getLyric, checkMusic } from "@/api/song.js"
import Vue from 'vue'
const playlist = {
  state: {
    currentIndex: -1,
    currentMusic: {},
    playlist: []
  },
  mutations: {
    SET_CURRENT_INDEX(state, idx) {
      state.currentIndex = idx;
    },
    SET_CURRENT_MUSIC(state, song) {
      state.currentMusic = song;
    },
    ADD_PLAYLIST(state, list) {
      const toString = (value) => Object.prototype.toString.call(value);
      const isArray = value => toString(value) == "[object Array]";
      if (isArray(list)) {
        let arr = [...state.playlist, ...list];
        //去重操作
        var obj = {};
        state.playlist = arr.reduce((cur,next) => {
          obj[next.id] ? "" : obj[next.id] = true && cur.push(next);
          return cur;
        },[])
      } else {
        state.playlist.push(list);
      }
    },
    CLEAR_PLAYLIST(state) {
      state.playlist.splice(0);
      state.currentIndex = -1;
      state.currentMusic = {};
    },
    DELETE_SONG(state, data) {
      if (data < state.currentIndex) {
        state.currentIndex -= 1;
      }
      state.playlist.splice(data, 1);
    }
  },
  actions: {
    SET_CURRENT_MUSIC_ACTION({ state,commit, dispatch }, data) {
      return new Promise(async (resolve, reject) => {
        //检查歌曲是否可用
        checkMusic(data.id).then(async(result) => {
          if (result.success) {
            //获取songUrl
            let res = await getSongUrl(data.id);
            let songList = res.data.map(item => {
              return { url: item.url, id: item.id };
            });
            data.url = songList[0].url;
            //获取歌词
            if (data.songType !== "dj") {
              let lyric = await getLyric(data.id);
              if(lyric.hasOwnProperty('lrc')){
                data.lrc = lyric.lrc.lyric;
              }
            }
            var colorThief = new ColorThief();
            colorThief.getColorAsync(data.cover, (color) => {
              data.theme = color;
            });
            let hasSong = false;
            let length = state.playlist.length;
            for (let i = 0; i < length; i++){
              if (data.id === state.playlist[i].id) {
                hasSong = true;
                commit("SET_CURRENT_MUSIC", data);
                commit("SET_CURRENT_INDEX", i);
                resolve(data);
                break;
              }
            }
            if (!hasSong) {
              commit("SET_CURRENT_MUSIC", data);
              commit("ADD_PLAYLIST", data);
              commit("SET_CURRENT_INDEX", length);
              resolve(data);
            }
          }
        }).catch((err) => {
          Vue.prototype.$message.warning('亲爱的，暂无版权。')
          reject("亲爱的，暂无版权");
        });
      })
    },
    NEXT_SONG({ state, commit, dispatch }) {
      return new Promise((resolve, reject) => {
        if (state.currentIndex === state.playlist.length - 1) {
          resolve(dispatch("SET_CURRENT_MUSIC_ACTION", state.playlist[0]));
        } else {
          resolve(dispatch("SET_CURRENT_MUSIC_ACTION", state.playlist[state.currentIndex + 1]));
        }
      })
    },
    LAST_SONG({ state, commit, dispatch }) {
      return new Promise((resolve, reject) => {
        if (state.currentIndex === 0) {
          resolve(dispatch("SET_CURRENT_MUSIC_ACTION", state.playlist[state.playlist.length - 1]));
        } else {
          resolve(dispatch("SET_CURRENT_MUSIC_ACTION", state.playlist[state.currentIndex - 1]));
        }
      })
    },
  }
}

export default playlist
