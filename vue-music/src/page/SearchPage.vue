<template>
  <div>
    <Header />
      <div>
        <div class="search-form">
          <el-input   class="search-input" v-model="searchVaue" placeholder="搜索音乐、歌手" suffix-icon="el-icon-search" @keyup.enter.native="submit"></el-input>
        </div>
      <div class="main">
        <div class="songlist_item odd clearfix">
            <div class="float-left songlist_name">歌曲</div>
            <div class="float-left songlist_album">歌手</div>
            <div class="float-left songlist_album">专辑</div>
            <div class="float-left songlist_time">时长</div>
        </div>
        <ul v-if="currentPage">
           <li :class="(index%2==0?'even ':'odd ') +' songlist_item clearfix'" v-for="(item, index) in currentPage" :key="index">
              <div class="songlist_index">{{ index+1 }}</div>
              <div v-if="item.banned" class=" songlist_name">
                  <span>{{ item.title }}</span>
                  <span class="banned">（无版权）</span>
              </div>
              <div v-else class="songlist_name">
                  <router-link target="_blank" v-bind:to="'/song/'+item.id">
                    <span>{{ item.title }}</span>
                  </router-link>
                  <router-link target="_blank" v-bind:to="'/play/song/'+item.id">
                    <span class="play"><i class="el-icon-service"></i></span>
                  </router-link>
              </div>
              <div class=" songlist_album">
                <router-link v-for="(singer, index) in item.artistArr" :key="index" :to="'/singer/'+singer.id">{{singer.name}}</router-link>
              </div>
              <div class=" songlist_album">{{ item.album }}</div>
              <div class=" songlist_time">{{ item.playTime }}</div>
          </li>
        </ul>
        <div v-if="currentPage" class="text-center">
           <el-pagination
              layout="prev, pager, next"
              :total="currentPage[0].songCount"
              :current-page="parseInt(pageIndex)"
              @current-change="getPageChange"
              class="text-center"
              >
            </el-pagination>
        </div>
      </div>

      </div>
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
  data(){
    return {
        searchVaue: '',
        size: 10,
        pageIndex: 0,
        currentPage: null,
        searchData: []
    }
  },
   methods: {
      getSearchKey(){
        return decodeURI(window.location.search.split('?key=')[1]) || null;
      },
      async getSearch(page=1){
         let key = this.getSearchKey();
          if(!key){
            return  this.$message({
                message: "访问格式出错",
                type: "error"
              });
          }
         let result = await this.$api.getSearch(key, this.size * (page-1), this.size);
         if(result.code === 200){
          this.currentPage = result.data;
          this.searchData[page]=result.data;
        }else{
          this.$message({
              message: "获取数据出错",
              type: "error"
            });
        }
      },
      submit(){
        this.$router.push(`/search?key=${this.searchVaue}`)
      },
      fetchData(){
        this.getSearch()
      },
      getPageChange(page){
        this.pageIndex=page;
        if(this.searchData[page]){
          this.currentPage= this.searchData[page];
          return false;
        }
        this.getSearch(page);
      },
    },
    created(){
      this.fetchData();
    },
    watch: {
      '$route': 'fetchData'
    },

}
</script>

<style scoped>
.search-form{
  position: relative;
  height: 247px;
  background-position: 50%;
  background-size: cover;
  background-image: url('../assets/images/bg_search.jpg');
  text-align: center;
  line-height: 247px
}
.search-input{
  width: 554px;
  height: 50px;
}

.cover{
    height: 330px;
    padding: 40px 0;
    background: #fafafa;
  }
  .show-img img{
    width: 250px;
    height: 250px;
    border-radius: 50%;
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
  .mod-data-item{
    display: inline-block;
    border-right: solid 1px #c9c9c9;
    text-align: center;
    padding-right: 20px;
    margin-right: 20px;
    font-size: 18px;
  }
  .play{
    color: #31c27c;
    font-size: 18px;
    margin-left: 20px;
    cursor: pointer;
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
    width: 500px;
    white-space: normal;
    padding-left: 4em;
    display: inline-block;
  }
  .songlist_album{
    padding-left: 20px;
    width:200px;
    display: inline-block;
  }
  .songlist_time{
    position: absolute;
    top: 0;
    right: 38px;
    width: 50px;
  }
  .banned{
    color: #C20C0C;
  }
</style>
