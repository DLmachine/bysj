import axios from 'axios';
import response from './response'
import moment from '../util/moment'
import host from '../../config/host'
export default class Api {

    //获取热门歌单
  static async getSonglist(offset, limit){
    let result = null;
    try {
      result = await axios(host + `personalized?offset=${offset}limit=${limit}&order=hot`);
    } catch (e) {
      console.log(e);
    }
    if (result.status === 200) {
      let data = result.data.result;
      return response(result.status, data)
    }
    return response(result.status, [])
  }

    //获取新歌
  static async getNewSong(){
    let result = null;
    try {
      result = await axios(host + "personalized/newsong");
    } catch (e) {
      console.log(e);
    }
    if (result.status === 200) {
      let data = result.data.result.map(item=>{
        let song ={};
        song.id = item.id;
        song.name = item.name
        song.picUrl = item.song.album.picUrl;
        song.singer = item.song.artists.map(item=>item.name).join('/');
        song.alias = item.song.alias;
        return song;
      })
      return response(result.status, data)
    }
    return response(result.status, [])
  }

  //获取热门mv
  static async getHotMv(offset, limit){
    let result = null;
    try {
      result = await axios(host + `top/mv?offset=${offset}&limit=${limit}`);
    } catch (e) {
      console.log(e)
    }
    if (result.status === 200) {
      let albums = result.data.data.map(item=>{
          let song ={};
          song.id = item.id;
          song.name = item.name;
          song.picUrl = item.cover;
          song.playCount = item.playCount;
          song.singer = item.artistName;
          return song;
      });
      return response(result.status, albums)
    }
    return response(result.status, [])
  }

  //获取新碟首发
  static async getHotAlbum(offset, limit){
    let result = null;
    try {
      result = await axios(host + `top/album?offset=${offset}&limit=${limit}`);
    } catch (e) {
      console.log(e)
    }
    if (result.status === 200) {
      let albums = result.data.albums.map(item=>{
          let song ={};
          song.id = item.id;
          song.name = item.name;
          song.picUrl = item.blurPicUrl;
          song.singer = item.artists.map(item=>item.name).join('/');
          song.alias = item.alias;
          return song;
      });
      return response(result.status, albums)
    }
    return response(result.status, [])
  }

  //获取热门歌手
  static async getHotArtists(offset, limit){
    let result = null;
    try {
      result = await axios(host + `top/artists?offset=${offset}&limit=${limit}`);
    } catch (e) {
      console.log(e)
    }
    if (result.status === 200) {
      let artists = result.data.artists.map(item=>{
          let artist ={};
          artist.id = item.id;
          artist.name = item.name;
          artist.picUrl = item.picUrl;
          artist.alias = item.alias;
          return artist;
      });
      return response(result.status, artists)
    }
    return response(result.status, [])
  }

  //获取最新唱片
  static async getNewAlbums(offset, limit){
    let result = null;
    try {
      result = await axios(host + `top/album?offset=${offset}&limit=${limit}`);
    } catch (e) {
      console.log(e)
    }
    if (result.status === 200) {
      let albums = result.data.albums.map(item=>{
        let album ={};
        album.id = item.id;
        album.name = item.name;
        album.picUrl = item.blurPicUrl;
        album.singer = item.artists.map(item=>item.name).join('/');
        album.alias = item.alias;
        return album;
      });
      return response(result.status, albums)
    }
    return response(result.status, [])
  }

  //获取单个歌手
  static async getSinger(id){
    let result = null;
    try {
      result = await axios(host + `artists?id=${id}`);
    } catch (e) {
      console.log(e)
    }
    if (result.status === 200) {
      let artist = {
        id: result.data.artist.id,
        picUrl: result.data.artist.picUrl,
        name: result.data.artist.name,
        desc: result.data.artist.briefDesc,
        albumSize: result.data.artist.albumSize,
        musicSize: result.data.artist.musicSize,
        mvSize: result.data.artist.mvSize,
      }
      let songlist = result.data.hotSongs.map(item=>{
          let song ={};
          song.id = item.id;
          song.title = item.name;
          song.picUrl = item.al.picUrl;
          song.album = item.al.name;
          song.alias = item.alias;
          song.playTime = moment.clock(item.dt);
          song.artist = item.ar.map(item=>item.name).join('/');
          song.lrc = `${this.host}lyric?id=${item.id}`;
          song.src = `http://music.163.com/song/media/outer/url?id=${
            item.id
          }.mp3`;
          song.banned = !!(item.st<=0 && item.fee <=0 )
          return song;
      });

      let singer ={artist, songlist}
      return response(result.status, singer)
    }
    return response(result.status, [])
  }

  //获取获取歌手 mv
  static async getSingerMV(id, pagesize=10){
    let result = null;
    try {
      result = await axios(host + `artist/mv?id=${id}`);
    } catch (e) {
      console.log(e)
    }
    if (result.status === 200) {
      let mvs = result.data.mvs.map(item=>{
          let mv ={};
          mv.id = item.id;
          mv.name = item.name;
          mv.picUrl = item.imgurl;
          mv.artists = item.artistName;
          mv.playTime = moment.clock(item.duration);
          mv.playCount = item.playCount;
          return mv;
      });
      let temp = [];
      let len = Math.floor(mvs.length / pagesize);
      for(let i=0; i< len; i++){
        temp.push(mvs.splice(0, pagesize))
      }
      return response(result.status, temp)
    }
    return response(result.status, [])
  }

    //获取排行榜
    static async getRank(id){
      let result = null;
      try {
        result = await axios(host + `top/list?idx=${id}`);
      } catch (e) {
        console.log(e)
      }
      if (result.status === 200) {
        let temp = [];
        let data = result.data.playlist.tracks;
        temp = data.map(item => {
          let song ={};
          song.id = item.id;
          song.title = item.al.name;
          song.picUrl = item.al.picUrl;
          song.album = item.al.name;
          song.alias = item.alias;
          song.playTime = moment.clock(item.dt);
          song.artist = item.ar.map(item=>item.name).join('/');
          song.lrc = `${this.host}lyric?id=${item.id}`;
          song.src = `http://music.163.com/song/media/outer/url?id=${
            item.id
          }.mp3`;
          song.banned = !!(item.st<0)
          return song;
        });
        return response(result.status, temp)
      }
      return response(result.status, [])
    }


    //获取电台分类
    static async getRadioCategory(){
      let result = null;
      try {
        result = await axios(host + `dj/catelist`);
      } catch (e) {
        console.log(e)
      }
      if (result.status === 200) {
        let radios = result.data.categories.map(item=>{
            let radio ={};
            radio.id = item.id;
            radio.name = item.name;
            radio.picUrl = item.picPCWhiteUrl;
            return radio;
        });
        return response(result.status, radios)
      }
      return response(result.status, [])
    }

    //获取电台推荐
    static async getRadio(id){
      let result = null;
      try {
        result = await axios(host + `dj/recommend/type?type=${id}`);
      } catch (e) {
        console.log(e)
      }
      if (result.status === 200) {
        let radios = result.data.djRadios.map(item=>{
            let radio ={};
            radio.id = item.id;
            radio.name = item.name;
            radio.category = item.category;
            radio.categoryId = item.categoryId;
            radio.picUrl = item.picUrl;
            radio.rcmdtext = item.rcmdtext;
            radio.programCount = item.programCount;
            return radio;
        })
        return response(result.status, radios)
      }
      return response(result.status, [])
    }
}
