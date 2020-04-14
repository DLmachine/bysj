<template>
  <div class="song-comment">
    <div class="write-comment-container">
      <a-row>
        <a-col :span="18" :offset="1">
          <a-textarea
            class="write-comment"
            placeholder="发表精彩评论"
            v-model="commentContent"
            :autosize="{ minRows: 4, maxRows: 4 }"
          />
        </a-col>
        <a-col :span="2">
          <a-button
            type="primary"
            class="comment-btn"
            :disabled="!this.commentContent"
            @click="comment"
          >发表</a-button>
        </a-col>
      </a-row>
    </div>
    <a-skeleton active :loading="loading">
      <div>
        <h1>
          <svg class="icon" aria-hidden="true" style="font-size:24px; margin:0 6px;">
            <use xlink:href="#icon-home_comment_fill" />
          </svg>&nbsp;热门评论
        </h1>
        <a-comment v-for="(item,index) in hotComments" :key="index" class="song-comment-list">
          <p slot="author" style="font-size:14px;">{{item.user.nickname}}</p>
          <a-avatar slot="avatar" :src="item.user.avatarUrl" alt="avatar" />
          <p slot="content">{{item.content}}</p>
          <a-comment v-for="(beReplied,idx) in item.beReplied" :key="idx">
            <p slot="author" style="font-size:14px;">{{beReplied.user.nickname}}</p>
            <a-avatar slot="avatar" :src="beReplied.user.avatarUrl" alt="avatar" />
            <p slot="content">{{beReplied.content}}</p>
          </a-comment>
        </a-comment>
      </div>
    </a-skeleton>
    <a-skeleton active :loading="loading">
      <div>
        <h1 style="margin-top:30px">
          <svg class="icon" aria-hidden="true" style="font-size:24px; margin:0 6px;">
            <use xlink:href="#icon-home_comment_fill" />
          </svg>&nbsp;最新评论
        </h1>
        <a-comment v-for="(item,index) in comments" :key="index" class="song-comment-list">

          <p slot="author" style="font-size:14px;">{{item.user.nickname}}</p>
          <a-avatar slot="avatar" :src="item.user.avatarUrl" alt="avatar" />
          <p slot="content">{{item.content}}</p>
          <a-comment v-for="(beReplied,idx) in item.beReplied" :key="idx">
            <p slot="author" style="font-size:14px;">{{beReplied.user.nickname}}</p>
            <a-avatar slot="avatar" :src="beReplied.user.avatarUrl" alt="avatar" />
            <p slot="content">{{beReplied.content}}</p>
          </a-comment>
        </a-comment>
      </div>
    </a-skeleton>
  </div>
</template>

<script>
import { getCommentMusic } from "@/api/song.js";
import { comment } from "@/api/comment.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      hotComments: [],
      comments: [],
      commentContent: "",
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {
    $route(to, from) {
      this.loading = true;
      this.getComments(to.query.id);
      this.loading = false;
    }
  },

  beforeMount() {},

  async mounted() {
    await this.getComments(this.$route.query.id);
    this.loading = false;
  },

  methods: {
    async getComments(data) {
      let res = await getCommentMusic(data);
      this.comments = res.comments;
      this.hotComments = res.hotComments;

    },
    async comment() {
      comment({
        type: 0,
        id: this.$route.query.id,
        content: this.commentContent.trim()
      })
        .then(async res => {
          this.$message.success("评论成功！");
          this.commentContent = "";
          this.loading = true;
          await this.getComments(this.$route.query.id);
          this.loading = false;
        })
        .catch(err => {
          if(err.response.status === 301) return;
          this.$message.error("因合作方要求，该资源不能评论");
        });
    }
  }
};
</script>
<style lang='scss' scoped>
.write-comment-container {
  position: relative;
  height: 130px;
  margin: 16px 0;
  .write-comment {
    display: block;
    margin: 16px auto;
  }
  .comment-btn {
    margin: 80px 0px 16px 16px;
  }
}
.song-comment {
  text-align: left;
  margin: 16px 0;
  padding-bottom: 100px;
  &-list {
    border-bottom: 1px dashed #ccc;
  }
  h1 {
    font-size: 24px;
    line-height: 2em;
    border-bottom: 1px solid #ccc;
  }
}
</style>
