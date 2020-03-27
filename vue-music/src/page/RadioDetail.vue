<template>
  <div>
    <Header />
      <div class="cover">
        <div class="main clearfix" v-if="radio">
          <div class="show-img float-left">
            <img :src="radio.picUrl" alt="">
          </div>
          <div class="singer-info float-left">
            <h1>{{ radio.name }}</h1>
            <p class="desc">{{ radio.desc.length>255?radio.desc.substr(0,255)+'...':radio.desc }}</p>
          </div>
        </div>
      </div>
      <div class="songlist main">
        <h2>节目列表</h2>
        <ul class="songlist_item odd clearfix">
            <li class="float-left songlist_name">节目名称</li>
            <li class="float-left songlist_album">所属</li>
            <li class="float-left songlist_time">时长</li>
        </ul>
        <div v-if="radio && radio.programs">
           <ul v-show="index<10 || showMore" :class="(index%2==0?'even ':'odd ') +' songlist_item clearfix'" v-for="(item, index) in radio.programs" :key="index">
              <li class="float-left songlist_index">{{ index+1 }}</li>
              <li class="float-left songlist_name">
                <router-link target="_blank" v-bind:to="'/play/song/'+item.id">
                  {{ item.title }}
                </router-link>
              </li>
              <li class="float-left songlist_album">{{ item.album }}</li>
              <li class="float-left songlist_time">{{ item.playTime }}</li>
          </ul>
        </div>
        <div class="songlist_item" v-else><span class="no-program">暂无免费节目</span></div>
      </div>
     <div v-if="radio.programs.length>10" class="text-center main"><el-button class="max-width" type="success" @click="getMore">{{showMore?"收起":"显示更多"}}</el-button></div>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'

import Footer from '../components/Footer'


export default {
  name: 'Artists',
  components: {
    Header,
    Footer,

  },
  async created(){
    let id = this.getPathIndex()
    this.getRadioDetail(id);
  },
  data(){
    return {
      radio: null,
      showMore: false
    }
  },
  methods: {
    getPathIndex(){
      return window.location.pathname.split('/radio_page/')[1]?window.location.pathname.split('/radio_page/')[1]:this.radioIndex;
    },
     getMore(){
      this.showMore = !this.showMore;
    },
    async getRadioDetail(id){
      let result = await this.$api.getRadioDetail(id);
      if(result.code === 200){
          this.radio=result.data;
      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    }
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
    margin-right: 2px;
    height: 104px;
    overflow: hidden;
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
  .mod-data-item{
    display: inline-block;
    border-right: solid 1px #c9c9c9;
    text-align: center;
    padding-right: 20px;
    margin-right: 20px;
    font-size: 18px;
  }
  .mod-data-item strong{
    font-size: 25px;
    font-weight: 400;
    margin-left: 10px;
  }
  .songlist h2{
    font-size: 24px;
    font-weight: 400;
    line-height: 58px;
  }
  .songlist_item{
    height: 50px;
    line-height: 50px;
    background-color: #fbfbfd;
    color: #999;
    position: relative;
  }
  .odd{
    background-color: #fbfbfd;
  }
  .even{
     background-color: #ffffff;
    color: #333;
  }
  .songlist_index{
    position: absolute;
    top: 0;
    left: 20px;
    color: #999;
    width: 36px;
  }
  .songlist_name{
    width: 47.685185%;
    white-space: normal;
    padding-left: 4em;
  }
  .songlist_album{
    padding-left: 20px;
    width: 25.5%;
  }
  .songlist_time{
    position: absolute;
    top: 0;
    right: 38px;
    width: 50px;
  }
  .no-program{
    color: #C20C0C;
  }
</style>

