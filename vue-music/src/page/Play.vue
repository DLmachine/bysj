<template>
  <div class="detail-container" v-bind:style="fullSceen">
    <div class="detail-header">
      <h1><router-link to="/">Ryan' music</router-link></h1>
    </div>
    <div class="main clearfix">
        <aplayer
          v-if="songlistData.length"
          :list="songlistData"
          autoplay
          preload="auto"
          :controls = true
          :showLrc= true
          :music="songlistData[currentMusicIndex]"
          :listMaxHeight="listHeight"
        />
        </div>
  </div>
</template>

<script>
import Header from "../components/Header";
import Aplayer from "vue-aplayer";

export default {
  name: "Play",
  components: {
    Header,
    Aplayer
  },
  async created() {
    let result = null;
    let match = window.location.pathname.split("/");
    let tyep = match[2];
    let id = match[3];
    let url = '';
    if(tyep === "song"){
        this.getSong(id);
    }else if(tyep === "songlist"){
        this.getSonglist(id);
    }else if(tyep === "album"){
        this.getAlbum(id);
    }else{
      if(this.$store.state.playlist.data){
        return this.songlistData = this.checkValidMusic(this.$store.state.playlist.data);
      }
      return  this.$message({
        message: "页面访问错误",
        type: "error"
      });
    }
       console.log(this.songlistData)

  },
  data() {
    return {
      currentMusicIndex: 0,
      songlistData: [],
      fullSceen: {
        height:
          (document.documentElement.clientHeight ||
            document.body.clientHeight) + "px",
        "overflow-y": "hidden"
      },
      listHeight: (document.documentElement.clientHeight || document.body.clientHeight) -65 -100 + "px",
    };
  },
  methods: {
    checkValidMusic(arr){
      return arr.filter(item=>!item.banned);
    },
    async getSonglist(id){
     let result = await this.$api.getSonglist(id);
     if(result.code === 200){
       this.songlistData = this.checkValidMusic(result.data);
     }
    },
    async getSong(id){
       let result = await this.$api.getSong(id);
        if(result.code === 200){
          this.songlistData = this.checkValidMusic(result.data);
        }
    },
    async getAlbum(id){
       let result = await this.$api.getAlbum(id);
        if(result.code === 200){
          this.songlistData = this.checkValidMusic(result.data);
        }
    }
  }
};
</script>

<style scoped>
.detail-container {
  background-color: #292a2b;
}
.detail-header h1 {
  margin: 0;
  padding: 10px 0;
  border-bottom: 1px solid #cccccc;

}
.detail-header h1 a{
  color: #ffffff;
}
.detail-header h1 a:hover{
    color: #31c27c;
}
.detail-header {
  color: #ffffff;
  text-align: center;
}
.music-list {
  color: #cccccc;
}
.music-list-item {
  font-size: 16px;
  margin: 15px 0;
  text-align: left;
}
.music-list-item a {
  color: #cccccc;
}
.music-list-item a:hover {
  color: #ffffff;
}
.song-name {
  display: inline-block;
  width: 390px;
}
.song-singer {
  display: inline-block;
  width: 180px;
}
.playTime {
  display: inline-block;
  width: 180px;
}
.lyrics {
  width: 350px;
}
</style>

