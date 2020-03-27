<template>
  <div class="recommend-wrap">
    <div class="singer-bg"></div>
    <div class="recommend">
      <h2 class="title">热门歌手</h2>
        <ul class="main clearfix">
          <li v-if="artists.length" v-for="(item, index) in currentPage" :key="index" class="song-menu-item  text-center">
          <div class="item-container">
              <div class="show-img ">
              <router-link v-bind:to="'/singer/'+item.id">
                  <img v-bind:src="item.picUrl" alt="">
                </router-link>
              </div>
              <h3 class="nowrap-text"><router-link v-bind:to="'/singer/'+item.id">{{ item.name }}</router-link></h3>
          </div>
          </li>
        </ul>
      <el-pagination
          layout="prev, pager, next"
          :total="100"
          :current-page="parseInt(pageIndex)"
          @current-change="getPageChange"
          class="text-center"
          >
        </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: "ArtistsComponent",
  created(){
    let page = window.location.pathname.split('/artists/')[1]?window.location.pathname.split('/artists/')[1]: 1;
    this.getHotArtists(page, this.limit, 10);
    window.data=this.artists;
  },
  methods: {
    async getHotArtists(page, limit, pagesize){
      let result = await this.$hotApi.getHotArtists((page-1) * limit, limit, pagesize);
      if(result.code === 200){
          this.pageIndex=page;
          this.artists[page] = result.data;
          this.currentPage=result.data;
      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    },
    getPageChange(page){
      this.$router.push(`/artists/${page}`)
      this.pageIndex=page;
      if(this.artists[page]){
        this.currentPage= this.artists[page];
        return false;
      }

      this.getHotArtists(page, this.limit, 10)
    }
  },
  data(){
    return {
      artists:[],
      offset:0,
      limit:10,
      pageIndex:0,
      currentPage: [],
    }
  }
};
</script>

<style scoped>
.recommend-wrap {
  background: #f5f5f5;
}
.recommend{
    padding: 20px;
}
.singer-bg{
  background: url('../assets/images/bg_singer.jpg') no-repeat;
  height: 400px;
  width: 100%;
  overflow: hidden;
}
.song-menu{
  height: auto;;
}
.title {
  font-size: 32px;
  text-align: center;
}
.song-menu-item {
    width: 20%;
    float: left;
    padding-left: 20px;
    min-height: 195px;
    overflow: hidden;
    margin-bottom: 30px;
}
.item-container{
  padding: 20px;
  background-color: #fbfbfd;
}
.show-img img{
  width: 145px;
  height: 145px;
  overflow: hidden;
  transition: all .3s;
  border-radius: 50%;
}

</style>
