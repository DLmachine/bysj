<template>
  <div>
    <Header />
      <div class="cover">
        <div class="main clearfix" v-if="data">
          <div class="show-img float-left">
            <img :src="data.pic" alt="">
          </div>
          <div class="singer-info float-left">
            <h1>{{ data.title }}</h1>
            <p class="desc"> 歌手：{{ data.artist }}</p>
            <p class="desc"> 发布时间：{{ data.publishTime }}</p>
             <div class="text-left"><span class="play_more_btn" @click="toPlay">播放</span></div>
          </div>
        </div>

      </div>
      <div class="lrc-container">
        <div class="main clearfix">
          <div  class="lrc">
            <h2>歌词</h2>
            <div class="lrc-box ">
              <p class="lrc-box-item" v-show="index<10 || showMore" v-for="(item, index) in lrc" :key="index">
                  {{ item }}
              </p>
              <div><span class="show-more"  @click="getMore">{{showMore?"[收起]":"[展开]"}}</span></div>
            </div>
          </div>
          <div class="float-left"><comment v-if="songId" type="music" :id="songId" size="10"/></div>
        </div>
      </div>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import Comment from '../components/Comment'

export default {
  name: 'Artists',
  components: {
    Header,
    Footer,
    Comment,
  },
  created(){
    const songId = window.location.pathname.split('/song/')[1];
    this.songId = songId;
    this.getSong(songId);
    this.getLrc(songId);

  },
  data(){
    return {
      data: null,
      showMore: false,
      songId: 0,
      lrc: [],
    }
  },
  methods:{
    async getSong(id){
      let result = await this.$api.getSong(id);
      if (result.code === 200) {
        this.data = result.data[0];
      }
    },
    async getLrc(id){
      let result = await this.$api.getLrc(id);
      if (result.code === 200) {
        this.lrc = result.data.replace(/\[(.)*\]/ig, "").split('\n');
      }
    },
    toPlay(){
      this.$store.commit("setPlaylist", {data:[this.data]})
      this.$router.push('/play');
    },
    getMore(){
      this.showMore = !this.showMore;
    },
  }


}
</script>

<style scoped>
  .cover{
    height: 330px;
    padding: 40px 0;
    background: #fafafa;
  }
  .show-img img{
    width: 250px;
    height: 250px;
  }
  .singer-info{
    width: 895px;
    padding-left: 65px;
  }
  .singer-info h1{
    font-size: 38px;
    font-weight: 400;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 90%;
    margin-right: 10px;
  }
  .singer-info .desc{
    max-width: 80%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-right: 2px;
  }
  .play_more_btn{
    min-width: 122px;
    text-align: center;
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
  .show-more{
    color: #31c27c;
    cursor: pointer;
  }
  .show-more:hover{
    color: #31c27c;
  }
  .lrc{
    float: left;
    width: 300px;
  }
  .lrc-box-item{
    width: 220px;
  }
  .lrc h2{
    font-size: 24px;
    font-weight: 400;
    line-height: 58px;
  }
  .odd{
    background-color: #fbfbfd;
  }
  .even{
     background-color: #ffffff;
    color: #333;
  }
  .lrc-container{
    background: #ffffff;
  }
  .lrc-box p{
    font-size: 14px;
    color: #000;
    line-height: 26px;
  }

</style>
