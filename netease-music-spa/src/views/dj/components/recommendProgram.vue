<template>
  <div>
    <a-row type="flex" justify="start" style="padding: 14px 0 0 0">
      <div class="dj-cate-top-title">
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>精彩节目推荐
      </div>
      <a-skeleton active :loading="loading">
        <div>
          <a-col :span="12" v-for="(item,index) in programRecommend" :key="index">
            <a-row type="flex" justify="start" class="recommend-new-songs">
              <a-col :span="3" style="position:relative;">
                <div @click.once="addMusic(item)">
                  <svg
                    class="icon play"
                    aria-hidden="true"
                    style="font-size:16px; margin-right:16px;"
                  >
                    <use xlink:href="#icon-play" />
                  </svg>
                  <img
                    v-lazy="item.cover"
                    width="100%"
                    alt="img"
                    style="margin:9px 0 0 9px;cursor: pointer;z-index:-1"
                  />
                </div>
              </a-col>
              <a-col :span="18" :offset="1">
                <p class="recommend-title">{{item.name}}</p>
                <p class="recommend-title" style="color:#999">{{item.artist}}</p>
              </a-col>
            </a-row>
          </a-col>
        </div>
      </a-skeleton>
    </a-row>
  </div>
</template>

<script>
import { getProgramRecommend } from "@/api/dj.js";
import Bus from "@/utils/bus.js";
import { mapActions } from "vuex";
export default {
  name: "",
  props: [""],
  data() {
    return {
      loading: true,
      programRecommend: []
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getProgramRecommend();
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getProgramRecommend() {
      let res = await getProgramRecommend();
      this.programRecommend = res.programs.map(item => {
        return {
          name: item.name,
          id: item.mainSong.id,
          artist: item.dj.nickname,
          artistId: item.radio.id,
          cover: item.coverUrl,
          theme: [255, 255, 255],
          songType: "dj"
        };
      });
    },
    async addMusic(song) {
      this.SET_CURRENT_MUSIC_ACTION(song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
<style lang='scss' scoped>
.dj-cate-top-title {
  text-align: left;
  width: 100%;
  font-size: 24px;
  line-height: 1.5em;
  border-bottom: 1px solid #dddddd;
  margin-bottom: 16px;
}
.dj-cate-list-title {
  font-size: 12px;
  cursor: text;
  line-height: 1.5em;
}
.recommend-title {
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.5em;
  cursor: text;
}
.recommend-new-songs {
  border-bottom: 1px solid #ddd;
  margin-right: 16px;
  .play {
    position: absolute;
    height: 50%;
    width: 50%;
    left: 40%;
    top: 25%;
    z-index: 9;
    cursor: pointer;
  }
}
</style>