<template>
  <div class="recommend-wrap">
    <div class="recommend">
    <div class="main">
        <h2 class="title">歌单分类</h2>
        <div class="category">
          <ul class="clearfix">
            <li v-if="calssifyCategory.length" v-for="(item, index) in calssifyCategory" :key="index" @click="active(index)" class="radio-menu-item  text-center">
              <h3 class="nowrap-text"><router-link v-bind:class="activeIndex===index?'nav-link-active':''"v-bind:to="'/classify/'+item.id">{{ item.name }}</router-link></h3>
            </li>
          </ul>
        </div>
        <div class="category">
          <ul class="clearfix">
            <li v-if="currentCategory.length" v-for="(item, index) in currentCategory" :key="index" @click="active1(index)" class="radio-menu-item  text-center">
              <h3 v-if="activeIndex==item.id"><router-link v-bind:class="active1Index===index?'nav-link-active':''"v-bind:to="'/classify/?cat='+item.name">{{ item.name }}</router-link></h3>

            </li>
          </ul>
        </div>
          <ul class="clearfix">
            <li v-if="currentData.length" v-for="(item, index) in currentData" :key="index" class="song-menu-item  text-center">
              <div class="show-img scale-img">
                <router-link v-bind:to="'/play/songlist/'+item.id">
                  <img v-bind:src="item.picUrl" alt="">
                   <div class="mask">
                    <i class="el-icon-caret-right"></i>
                  </div>
                </router-link>
              </div>
              <h3 class="nowrap-text"><router-link v-bind:to="'/play/songlist/'+item.id">{{ item.name }}</router-link></h3>
            </li>
          </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ClassifyComponent",
  async created(){

      await this.getClassifyCategory();
      const calssifyTypeId = this.getPathIndex();
      await this.getCalssify(calssifyTypeId)

  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    getPathIndex(){
      let temp=null;

      for(var item in this.currentCategory){
        if(this.currentCategory[item].id==this.activeIndex){
          temp=this.currentCategory[item];
          break;
        }
      }
      let data=document.URL.split('/classify/?')[1]?document.URL.split('/classify/')[1]:"?cat="+temp.name;
      console.log(this.currentCategory,this.activeIndex,data)
      return data;
    },
    active(index) {
      this.activeIndex = index;
    },
    active1(index) {
      this.active1Index = index;
    },
    async getClassifyCategory(){
      let result = await this.$hotApi.getClassifyCategory();
      if(result.code === 200){
          this.currentCategory=result.data;

      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    },
    async getCalssify(id){
      console.log(window.location.pathname.split('/classify'))
      let result = await this.$hotApi.getCalssify(id);
      if(result.code === 200){
          this.currentData=result.data;
      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    },
    fetchData(){
      let calssifyTypeId = this.getPathIndex();
      this.getCalssify(calssifyTypeId);
    }
  },
  data(){
    return {
      album:[],
      offset:0,
      limit:10,
      radioIndex:10001,
      currentPage: [],
      activeIndex:0,
      active1Index:0,
      calssifyCategory: [{id:'0',name:"语种"},{id:'1',name:"风格"},{id:'2',name:"场景"},{id:'3',name:"情感"},{id:'4',name:"主题"}],
      currentData: [],
      currentCategory:[]
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
.nav-link-active {
  background-color: #cfcfcf;
  color: #fff !important;
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
