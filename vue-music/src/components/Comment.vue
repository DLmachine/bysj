<template>
  <div class="comment-container" v-if="currentPage">
    <h2 class="title"><span>评论 </span> <span class="total"></span><small>共{{currentPage.total}}条 评论</small></h2>
    <div class="comment">
      <h3>热门评论</h3>
      <ul class="comment-wrap">
         <li v-for="(item, index) in comments.hotComments" :key="index" class="comment-item">
            <div class="comment-avatar"><img :src="item.user.avatar" alt=""></div>
            <div class="comment-user">{{item.user.name}}</div>
            <div class="content">{{item.content}}</div>
            <div class="comment-footer"><span class="comment-date">{{item.time}}</span><span><i class="el-icon-star-off"></i> {{item.likedCount}}</span></div>
         </li>
      </ul>
      <h3 id="new_comment">最新评论</h3>
      <ul class="comment-wrap">
         <li v-for="(item, index) in currentPage.comments" :key="index" class="comment-item">
            <div class="comment-avatar"><img :src="item.user.avatar" alt=""></div>
            <div class="comment-user">{{item.user.name}}</div>
            <div class="content">{{item.content}}</div>
            <div class="comment-footer"><span class="comment-date">{{item.time}}</span><span><i class="el-icon-star-off"></i> {{item.likedCount}}</span></div>
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
  created(){
    this.getComment();
  },
  props: ["type", "id", "size"],
  data(){
    return {
      comments: {
        comments: [],
        hotComments: [],
      },
      pageIndex: 1,
      currentPage: null,
      scrollEle: null
    }
  },
  methods: {
    async getComment(){
      let result = await this.$api.getComment(this.type, this.id, (this.pageIndex -1) * this.size,  this.size);
      if (result.code === 200) {
       this.currentPage=  result.data;
       this.comments.comments[this.pageIndex] = result.data.comments;
       if(result.data.hotComments){
         this.comments.hotComments = result.data.hotComments;
       }
      }
    },
    async getPageChange(page){
      this.pageIndex=page;
      if(this.comments[page]){
        this.currentPage= this.comments.comments[page];
        return false;
      }
      await this.getComment();
      if(!this.scrollEle){
        this.scrollEle=document.getElementById('new_comment');
      }
      this.scrollEle.scrollIntoView()
    }
  }
}
</script>

<style scoped>
  .title{
    font-size: 24px;
    font-weight: 400;
    line-height: 58px;
  }
  .comment h3{
    font-weight: 400;
    font-size: 16px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .total{
    font-size: 14px;
    margin-left: 12px;
    color: #999999;
  }
  .comment-avatar {
      position: absolute;
      left: 0;
      top: 20px;
      width: 38px;
      height: 38px;
  }
  .comment-avatar img{
    display: block;
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }
  .comment-item{
    position: relative;
    padding: 15px 0 15px 56px;
    zoom: 1;
    border-bottom-width: 1px;
    border-bottom-style: solid;
    border-color: #ededed;
  }
  .comment-user{
    font-weight: 400;
    margin-bottom: 6px;
    overflow: hidden;
    height: 20px;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
  .comment-comment {
    overflow: hidden;
    word-break: break-all;
    word-wrap: break-word;
    line-height: 24px;
    text-align: justify;
  }
  .comment-footer{
    line-height: 24px;
    text-align: right;
    overflow: hidden;
  }
  .comment-date {
    float: left;
    line-height: 28px;
  }
  .comment-wrap{
    width: 850px;
  }
</style>
