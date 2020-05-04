<template>
  <div class="mv-comment">
    <h1>
      <svg class="icon" aria-hidden="true" style="font-size:24px; margin:0 6px;">
        <use xlink:href="#icon-home_comment_fill" />
      </svg>&nbsp;热门评论
    </h1>
    <a-comment v-for="(item,index) in hotComments" :key="index" class="mv-comment-list">
      <a slot="author">{{item.user.nickname}}</a>
      <a-avatar slot="avatar" :src="item.user.avatarUrl" alt="avatar" />
      <p slot="content">{{item.content}}</p>
      <a-comment v-for="(beReplied,idx) in item.beReplied" :key="idx">
        <a slot="author">{{beReplied.user.nickname}}</a>
        <a-avatar slot="avatar" :src="beReplied.user.avatarUrl" alt="avatar" />
        <p slot="content">{{beReplied.content}}</p>
      </a-comment>
    </a-comment>
  </div>
</template>

<script>
import { getCommentMv, getCommentVideo } from "@/api/mv.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      hotComments: [],
    };
  },

  computed: {
    videoType(){
      return this.$route.query.type;
    }
  },

  async mounted() {
    if(this.videoType == "mv"){
      await this.getCommentMv();
    } else if (this.videoType == "video") {
      await this.getCommentVideo();
    }
  },

  methods: {
    async getCommentMv() {
      let res = await getCommentMv(this.$route.query.id);
      this.hotComments = [...res.hotComments,...res.comments];
    },
    async getCommentVideo() {
      let res = await getCommentVideo(this.$route.query.id);
      this.hotComments = [...res.hotComments,...res.comments];
    }
  }
};
</script>
<style lang='scss' scoped>
.mv-comment {
  text-align: left;
  margin: 16px 0;
  padding-bottom: 100px;
  &-list{
    border-bottom: 1px dashed #ccc;
  }
  h1 {
    font-size: 24px;
    line-height: 2em;
    border-bottom: 1px solid #ccc;
  }
}
</style>