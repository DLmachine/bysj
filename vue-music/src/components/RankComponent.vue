<template>
  <div class=" rank-container">
     <div  class="main  clearfix">
        <div class="tabnav float-left">
          <ul >
            <li class="rank-header">音乐巅峰榜</li>
            <li  @click="()=>changeIndex(index)" v-for="(item, index) in rankarr" :key="index" :class="index===activeIndex?'active-item':''"><span>{{item}}</span></li>
          </ul>
        </div>
        <div class="rank-content float-left">
            <el-table
                v-loading="loading"
                element-loading-text="拼命加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(0, 0, 0, 0.8)"
                :data="[]"
                style="width: 100%; heoght:200px"
                v-if="!currentRankData"
                >
            </el-table>
           <ul v-if="currentRankData" >
            <li class="rank-header">巅峰榜·流行指数 {{ getNowFormatDate() }} 榜单规则   </li>
            <li class="rank-header text-left"><span class="play_more_btn" @click="toPlay">播放全部单曲</span></li>
            <li v-for="(item, index) in currentRankData" :key="index" :class="(index%2==0?'even ':'odd ') +' rank-item clearfix'">
              <div class="float-left song-index">{{ index +1}}</div>
              <div v-if="item.banned"  class="float-left song-name">
                <router-link target="_blank" v-bind:to="'/song/'+item.id">
                  <img :src="item.picUrl" alt="">
                  <span class="banned">（无版权）</span>
                </router-link>
              </div>
              <div v-else class="float-left song-name">
                <router-link target="_blank" v-bind:to="'/song/'+item.id">
                  <img :src="item.picUrl" alt="">
                  <span>{{ item.title }}</span>
                </router-link>
                <router-link target="_blank" v-bind:to="'/play/song/'+item.id">
                  <span class="play"><i class="el-icon-service"></i></span>
                </router-link>
              </div>
              <div class="float-left song-artist v-mid nowrap-text">{{item.artist}}</div>
              <div class="float-left song-time">{{item.playTime}}</div>
            </li>

          </ul>
        </div>

     </div>
  </div>
</template>

<script>
import moment from '../util/moment'
const rankarr={
  "0":" 云音乐新歌榜",
  "1":" 云音乐热歌榜",
  "2":" 网易原创歌曲榜",
  "3":" 云音乐飙升榜",
  "4":" 云音乐电音榜",
  "5":" UK排行榜周榜",
  "6":" 美国Billboard周榜",
  "7":" KTV嗨榜",
  "8":" iTunes榜",
  "9":" Hit FM Top榜",
  "10":" 日本Oricon周榜",
  "11":" 韩国Melon排行榜周榜",
  "12":" 韩国Mnet排行榜周榜",
  "13":" 韩国Melon原声周榜",
  "14":" 中国TOP排行榜(港台榜)",
  "15":" 中国TOP排行榜(内地榜)",
  "16":" 香港电台中文歌曲龙虎榜",
  "17":" 华语金曲榜",
  "18":" 中国嘻哈榜",
  "19":" 法国 NRJ EuroHot 30周榜",
  "20":" 台湾Hito排行榜",
  "21":" Beatport全球电子舞曲榜",
  "22":" 云音乐ACG音乐榜",
  "23":" 云音乐嘻哈榜"
  }

export default {
 data() {
      return {
        rankarr: [],
        activeIndex: 0,
        loading: false,
        currentRankData: null
      };
    },
    created(){
      this.rankarr = Object.values(rankarr);
      this.getRank(0);
    },
    methods: {
      changeIndex(index) {
        this.activeIndex = index;
        this.getRank(index)
      },
      async getRank(id){
       if(!!this.$store.state.rankData.data[id]){
         return this.currentRankData = this.$store.state.rankData.data[id];
       }
       this.loading=true;
       this.currentRankData=null;
       let result = await this.$hotApi.getRank(id);
        if(result.code === 200){
          this.$store.commit("setRankData", {id, data: result.data});
          this.currentRankData = result.data;
        }else{
          this.$message({
              message: "获取数据出错",
              type: "error"
            });
        }
        this.loading=false;
      },
       getNowFormatDate() {
          return moment.getNowFormatDate();
      },
      toPlay(){
        this.$store.commit("setPlaylist", {data:this.currentRankData})

        this.$router.push('/play');
      }
    }
}
</script>

<style scoped>
.rank-container{
  padding: 0 20px;
  background: url('../assets/images/bg_detail.jpg') repeat-x;
}
.tabnav{
  width: 178px;
  border-width: 1px;
  border-style: solid;
  border-color: rgba(153,153,153,.2);
}
.tabnav span{
    font-size: 15px;
    display: block;
    line-height: 22px;
    padding: 8px 17px;
    cursor: pointer;
}
.active-item{
   background-color: #31c27c;
    color: #fff;
}
.tabnav span:hover{
    background-color: #31c27c;
    color: #fff;
}
.rank-header{
  line-height: 60px;
    font-size: 20px;
    font-weight: 400;
    border-bottom: 1px solid #ebebeb;
    text-align: center;
}

.rank-content{
  width: 900px;
  margin-left: 40px;
}
.rank-item{
  height: 80px;
  line-height: 80px;
  overflow: hidden;
}
.song-index{
  width: 60px;
  text-align: right;
  font-size: 24px;
  color: #333;

}
.song-name{
  width: 550px;
  float: left;
  padding-left: 80px;
}
.song-name img{
  width: 70px;
  height: 70px;
  vertical-align: middle;
  margin-right: 20px;
}
.song-artist{
  margin-right: 20px;
  width: 200px;
  float: left;
  padding-right: 30px;
}
.odd{
  background-color: #fbfbfd;
}
.even{
  color: #333;
}
.banned{
  color: #C20C0C;
}
.play{
    color: #31c27c;
    font-size: 18px;
    margin-left: 20px;
    cursor: pointer;
}
.play_more_btn{
  min-width: 122px;
  text-align: left;
  border: 1px solid #31c27c;
  background-color: #31c27c;
  color: #fff;
  cursor: pointer;
  border-radius: 2px;
  font-size: 14px;
  margin-right: 6px;
  padding: 0 23px;
  height: 38px;
  line-height: 38px;
  display: inline-block;
  white-space: nowrap;
  box-sizing: border-box;
  overflow: hidden;
  margin-top: 20px;
  transition: all .3s;
}
.play_more_btn:hover{
    background-color: #009a61;
}
</style>

