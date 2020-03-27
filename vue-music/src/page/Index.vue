<template>
  <div>
    <Header />
    <SongListRecommend :songlist="songlist"/>
    <NewSongRecommend :newSongList="newSongList"/>
    <NewAlbum  :albumsList="albumsList"/>
    <MV :MvList="MvList"/>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import SongListRecommend from '../components/SongListRecommend'
import NewSongRecommend from '../components/NewSongRecommend'
import NewAlbum from '../components/NewAlbum'
import MV from '../components/MV'
import Footer from '../components/Footer'
import splitArray from '../util/splitArray'

export default {
  name: 'Index',
  components: {
    Header,
    SongListRecommend,
    NewSongRecommend,
    NewAlbum,
    MV,
    Footer
  },
  data(){
    return {
      songlist: [],
      albumsList: [],
      MvList: [],
      newSongList: [],
    }
  },
  async created(){
    await this.getSonglist(0, 20, 5)
    await this.getMv(0, 80, 10);
    await this.getAlbum(0,20, 5);
    await this.getNewSong(9);
  },
  methods: {
    async getSonglist(offset, limit, pagesize){
      let result = await this.$hotApi.getSonglist(offset, limit);
      if(result.code === 200){
          this.songlist =splitArray(result.data, pagesize)
        }else{
          this.$message({
              message: "获取数据出错",
              type: "error"
            });
        }
    },
    async getNewSong(pagesize){
      let result = await this.$hotApi.getNewSong();
      if(result.code === 200){
          this.newSongList = splitArray(result.data, 9);
        }else{
          this.$message({
              message: "获取数据出错",
              type: "error"
            });
        }
    },
    async getMv(offset, limit, pagesize){
      let result = await this.$hotApi.getHotMv(offset, limit);
      if(result.code === 200){
          this.MvList = splitArray(result.data, pagesize);
        }else{
          this.$message({
              message: "获取数据出错",
              type: "error"
            });
        }
    },
    async getAlbum(offset, limit, pagesize){
      let result = await this.$hotApi.getHotAlbum(offset, limit);
      if(result.code === 200){
          this.albumsList = splitArray(result.data, pagesize);
        }else{
          this.$message({
              message: "获取数据出错",
              type: "error"
            });
        }
    }
  },


}
</script>

<style>

</style>
