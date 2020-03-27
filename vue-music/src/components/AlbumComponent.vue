<template>
  <div class="recommend-wrap">
    <div class="recommend">
    <h2 class="title">推荐歌单</h2>
      <ul class="main clearfix">
        <li v-if="album.length" v-for="(item, index) in currentPage" :key="index" class="song-menu-item  text-center">
          <div class="show-img ">
            <router-link target="_blank" v-bind:to="'/play/album/'+item.id">
              <img v-bind:src="item.picUrl" alt="">
              <div class="mask">
                <i class="el-icon-caret-right"></i>
              </div>
            </router-link>
          </div>
          <h3 class="nowrap-text"><router-link v-bind:to="'/play/album/'+item.id">{{ item.name }}</router-link></h3>
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
  name: "AlbumComponent",
  created(){
    let page = window.location.pathname.split('/album/')[1]?window.location.pathname.split('/album/')[1]: 1;
    this.getNewAlbums(page, this.limit, 10);
  },
  methods: {
    async getNewAlbums(page, limit, pagesize){
      let result = await this.$hotApi.getNewAlbums((page-1) * limit, limit, pagesize);
      if(result.code === 200){
          this.pageIndex=page;
          this.album[page] = result.data;
          this.currentPage=result.data;
      }else{
        this.$message({
            message: "获取数据出错",
            type: "error"
          });
      }
    },
    getPageChange(page){
      this.$router.push(`/album/${page}`)
      this.pageIndex=page;
      if(this.album[page]){
        this.currentPage= this.album[page];
        return false;
      }

      this.getNewAlbums(page, this.limit, 10)
    }
  },
  data(){
    return {
      album:[],
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
.song-menu-item {
  width: 20%;
  float: left;
  padding: 0 10px;
  margin-bottom: 30px;
}
.show-img{
  position: relative;
  width: 230px;
  height: 230px;
  overflow: hidden;
  transition: all .3s;
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
  padding-top: 70px;

}

</style>
