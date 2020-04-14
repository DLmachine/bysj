<template>
  <div>
    <a-row>
      <a-col :span="24">
        <a-skeleton active :loading="loading">
          <a-row type="flex" justify="start" style="margin-top:30px">
            <a-col :span="23" :offset="1" class="title">
              <span>每日推荐歌单</span>
            </a-col>
            <a-col
              :span="5"
              :offset="1"
              class="play-list-item"
              v-for="(item,index) in dailyPlaylist"
              :key="index"
              @click="goPlaylistDetail(item)"
            >
              <div class="img-box">
                <img v-lazy="item.picUrl" width="100%" alt="img" />
              </div>
              <p class="play-list-title">{{item.name}}</p>
            </a-col>
          </a-row>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getRecommendResource } from "@/api/playList";
export default {
  name: "",
  props: [""],
  data() {
    return {
      dailyPlaylist: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getRecommendResource();
    this.loading = false;
  },

  methods: {
    async getRecommendResource() {
      let res = await getRecommendResource();
      this.dailyPlaylist = res.recommend;
    },
    goPlaylistDetail(data) {
      this.$router.push({
        path: "/playlist-detail",
        query: {
          id: data.id
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.img-box {
  width: 100%;
  position: relative;
  height: 0;
  padding-bottom: 100%;
  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
  }
}
.play-list-item {
  margin-top: 16px;
  .play-list-title {
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
}
.title {
  text-align: left;
  font-size: 16px;
  font-weight: bold;
  margin-top: 22px;
}
</style>