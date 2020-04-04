import axios from 'axios';
import response from './response'
import moment from '../util/moment'
import host from '../../config/host'
export default class Api {
  //获取单首歌曲
  static async getSong(id){
    let result = {};
    let url =host + `song/detail?ids=${id}`
    try {
      result = await axios(url);
    } catch (e) { }
    if(result.status === 200){
      let data = result.data.songs[0];
      console.log(data)
      window.data=data
        let song = {};
        song.id = data.id;
        song.title = data.name;
        song.artist = data.ar.map(item => item.name).join(" / ");
        song.singerId = data.ar.map(data => data.id);
        song.src = `http://music.163.com/song/media/outer/url?id=${
          data.id
        }.mp3`;
        song.publishTime = moment.formatDate(data.publishTime);
        song.lrc = `${host}lyric?id=${data.id}`;
        song.pic = data.al.picUrl;

      return response(200, [song])
    }
    return response(result.status, [])
  }

  //获取歌单
  /**
   *
   * @param {*} id
   */
   static async getSonglist(id){
    let result = {};
    let url =host + `playlist/detail?id=${id}`
    try {
      result = await axios(url);
    } catch (e) {

    }
    if(result.status === 200){
      let temp = [];

      let data = result.data.playlist.tracks;
      console.log(data)
      temp = data.map(item => {
        let song = {};
        song.id = item.id;
        song.title = item.name;
        song.artist = item.ar.map(item => item.name).join(" / ");
        song.singerId = item.ar.map(item => item.id);
        song.src = `http://music.163.com/song/media/outer/url?id=${
          item.id
        }.mp3`;
        song.lrc = `${host}lyric?id=${item.id}`;
        song.pic;
        return song;
      });
      return response(200, temp)
    }
    return response(result.status, [])
  }

  //获取MV
  static async getMV(id){
    let result = {};
    let url =host + `mv/detail?mvid=${id}`
    try {
      result = await axios(url);
    } catch (e) {

    }
    if(result.status === 200){
      let temp = [];
      let data = result.data.data;
      console.log(data)
      let song = {};
      song.id = data.id;
      song.title = data.name;
      song.artist = data.artists.map(item => item.name).join(" / ");
      song.singerId = data.artistName;
      song.src = Object.values(data.brs)[Object.keys(data.brs).length-1];
      song.lrc = `${host}lyric?id=${data.id}`;
      song.pic = data.cover;

      return response(200, song)
    }
    return response(result.status, null)
  }

  //获取专辑
  static async getAlbum(id){
    let result = {};
    let url =host + `album?id=${id}`
    try {
      result = await axios(url);
    } catch (e) {

    }
    if(result.status === 200){
      let temp = [];
      let data = result.data.songs;
      temp = data.map(item => {
        let song = {};
        song.id = item.id;
        song.title = item.al.name;
        song.artist = item.ar.map(item => item.name).join(" / ");
        song.singerId = item.ar.map(item => item.id);
        song.src = `http://music.163.com/song/media/outer/url?id=${
          item.id
        }.mp3`;
        song.lrc = `${host}lyric?id=${item.id}`;
        song.pic;
        return song;
      })
      return response(200, temp)
    }
    return response(result.status, null)
  }

    //获取电台详情
    static async getRadioDetail(id){
      let result = {};
      let url =host + `dj/detail?rid=${id}`
      try {
        result = await axios(url);
      } catch (e) { }
      //获取电台节目
      let program = null;
      let programRs = {};
      try {
        programRs = await axios(host + `dj/program?rid=${id}&limit=100`);
      } catch (e) { }
      if(programRs.status === 200){
        program = programRs.data.programs;
      }else{
        return response(result.status, [])
      }

      if(result.status === 200){
        let data = result.data.djRadio;
          let radio = {};
          radio.id = data.id;
          radio.name = data.name;
          radio.desc = data.desc;
          radio.category = data.category;
          radio.rcmdText = data.rcmdText;
          radio.programs = program?program.map(item=>{
            let program = {};
            program.id = item.mainSong.id;
            program.title = item.name;
            program.artist = item.dj.nickname;
            program.singerId = null;
            program.album = data.name;
            program.playTime = moment.clock(item.duration);
            program.src = `http://music.163.com/song/media/outer/url?id=${
              item.mainSong.id
            }.mp3`;
            program.lrc = `${host}lyric?id=${item.mainSong.id}`;
            program.picUrl = item.coverUrl;
            return program;
          }).reverse():null;
          radio.picUrl = data.picUrl;
        return response(200, radio)
      }
      return response(result.status, [])
    }

  static async getClassifyDetail(id){
      let result = {};
      let url =host + `dj/detail?rid=${id}`
      try {
        result = await axios(url);
      } catch (e) { }
      //获取电台节目
      let program = null;
      let programRs = {};
      try {
        programRs = await axios(host + `dj/program?rid=${id}&limit=100`);
      } catch (e) { }
      if(programRs.status === 200){
        program = programRs.data.programs;
      }else{
        return response(result.status, [])
      }

      if(result.status === 200){
        let data = result.data.djRadio;
          let radio = {};
          radio.id = data.id;
          radio.name = data.name;
          radio.desc = data.desc;
          radio.category = data.category;
          radio.rcmdText = data.rcmdText;
          radio.programs = program?program.map(item=>{
            let program = {};
            program.id = item.mainSong.id;
            program.title = item.name;
            program.artist = item.dj.nickname;
            program.singerId = null;
            program.album = data.name;
            program.playTime = moment.clock(item.duration);
            program.src = `http://music.163.com/song/media/outer/url?id=${
              item.mainSong.id
            }.mp3`;
            program.lrc = `${host}lyric?id=${item.mainSong.id}`;
            program.picUrl = item.coverUrl;
            return program;
          }).reverse():null;
          radio.picUrl = data.picUrl;
        return response(200, radio)
      }
      return response(result.status, [])
    }
    //获取搜索
  static async getSearch(key, offset, limit) {
    let result = {};
    let url =host + `search?keywords=${key}&offset=${offset}&limit=${limit}`
    try {
      result = await axios(url);
    } catch (e) {

    }
    if(result.status === 200){
      let temp = [];
      let data = result.data.result.songs;
      temp = data.map(item => {
        let song = {};
        song.songCount = result.data.result.songCount;
        song.id = item.id;
        song.title = item.name;
        song.album = item.album.name;
        song.artist = item.artists.map(item => item.name).join("/");
        song.artistArr = item.artists;
        song.singerId = item.artists.map(item => item.id);
        song.playTime = moment.clock(item.duration);
        song.src = `http://music.163.com/song/media/outer/url?id=${
          item.id
        }.mp3`;
        song.lrc = `${host}lyric?id=${item.id}`;
        song.banned = !!(item.fee<=0)
        song.pic;
        return song;
      })
      return response(200, temp)
    }
    return response(result.status, null)
  }

  static async getLrc(id){
    let result = {};
    let url =`${host}lyric?id=${id}`;
    try {
      result = await axios(url);
    } catch (e) {

    }
    if(result.status === 200){
      let lrc = result.data.lrc.lyric;
      return response(200, lrc)
    }
    return response(result.status, null)
  }

  //获取评论
  /**
   *
   * @param {*} type
   * @param {*} id
   * @param {*} offset
   * @param {*} limit
   */
  static async getComment(type, id, offset, limit){
    let result = {};
    let url =host + `comment/${type}?id=${id}&offset=${offset}&limit=${limit}`
    try {
      result = await axios(url);
    } catch (e) {

    }
    console.log(result)
    if(result.status === 200){
      let temp = {};
      let data = result.data;
      temp.total = data.total;
      temp.comments = data.comments.map(item => {
        let comment = {};
        comment.id = item.commentId;
        comment.content = item.content;
        comment.likedCount = item.likedCount;
        comment.time = moment.formatDate(item.time);
        comment.user = {
          id:  item.user.userId,
          name:  item.user.nickname,
          avatar:  item.user.avatarUrl,
        }
        return comment;
      })
      temp.hotComments = data.hotComments?data.hotComments.map(item => {
        let comment = {};
        comment.id = item.commentId;
        comment.content = item.content;
        comment.likedCount = item.likedCount;
        comment.time = moment.formatDate(item.time);
        comment.user = {
          id:  item.user.userId,
          name:  item.user.nickname,
          avatar:  item.user.avatarUrl,
        }
        return comment;
      }):null;
      return response(200, temp)
    }
    return response(result.status, null)
  }
}
