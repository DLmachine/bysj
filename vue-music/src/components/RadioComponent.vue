<template>
  <div class="recommend-wrap">
    <div class="recommend">
    <div class="main">
        <h2 class="title">电台</h2>
        <div class="category">
          <ul class="clearfix">
            <li v-if="radioCategory.length" v-for="(item, index) in radioCategory" :key="index" class="radio-menu-item  text-center">
              <h3 class="nowrap-text"><router-link v-bind:to="'/radio/'+item.id">{{ item.name }}</router-link></h3>
            </li>
          </ul>
        </div>
          <ul class="clearfix">
            <li v-if="currentData.length" v-for="(item, index) in currentData" :key="index" class="song-menu-item  text-center">
              <div class="show-img scale-img">
                <router-link v-bind:to="'/radio_page/'+item.id">
                  <img v-bind:src="item.picUrl" alt="">
                   <div class="mask">
                    <i class="el-icon-caret-right"></i>
                  </div>
                </router-link>
              </div>
              <h3 class="nowrap-text"><router-link v-bind:to="'/radio_page/'+item.id">{{ item.name }}</router-link></h3>
            </li>
          </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AlbumComponent",
  async created(){
      const radioTypeId = this.getPathIndex();
      await this.getRadioCategory()
      await this.getRadio(radioTypeId);

  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    getPathIndex(){
      return window.location.pathname.split('/radio/')[1]?window.location.pathname.split('/radio/')[1]:this.radioIndex;
    },
    async getRadio(id){
      let result = await this.$hotApi.getRadio(id);
      if(result.code === 200){
          this.currentData=result.data;
      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    },
    async getRadioCategory(){
      let result = await this.$hotApi.getRadioCategory();
      if(result.code === 200){
          this.radioCategory=result.data;
      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    },
    fetchData(){
      let radioTypeId = this.getPathIndex();
      this.getRadio(radioTypeId);
    }
  },
  data(){
    return {
      album:[],
      offset:0,
      limit:10,
      radioIndex:10001,
      currentPage: [],
      radioCategory: [],
      currentData: [],
    }
  }
};
</script>

<style scoped>
.recommend-wrap {
  background: #ffffff;
  padding: 20px;
}
.recommend {
}
.song-menu{
  height: auto;;
}
.title {
  font-size: 32px;
  text-align: center;
}
.radio-menu-item {
  width: 10%;
  float: left;
  padding: 0 10px;
}
.song-menu-item {
  width: 20%;
  float: left;
  padding: 0 10px;
  margin-bottom: 30px;
}
.show-img{
  width: 220px;
  height: 220px;
  overflow: hidden;
  transition: all .3s;
  position: relative;
}
.show-img img{
  width: 220px;
  height: 220px;
}
.show-img:hover .mask{
  opacity: 1;
}
.mask{
  opacity: 0;
  transition: all .3s;
  position: absolute;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.6);
  top: 0;
  left: 0;
  color: #ffffff;
  font-size: 60px;
  padding-top: 65px;

}
</style>
