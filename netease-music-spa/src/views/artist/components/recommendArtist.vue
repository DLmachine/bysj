<template>
  <div class="artist">
    <a-skeleton active :loading="loading">
      <div class="artist-list">
        <div
          style="
            text-align: left;
            width: 100%;
            font-size: 24px;
            line-height: 1.5em;
            border-bottom: 1px solid #dddddd;
            margin-bottom: 16px;"
        >
          <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
            <use xlink:href="#icon-circle" />
          </svg>入驻歌手
        </div>
        <a-row type="flex" justify="space-around">
          <a-col
            :span="4"
            style="margin:0 2px 16px 0"
            class="artist-list-item"
            v-for="(item,index) in residentSinger"
            :key="index"
          >
            <div class="img-box">
              <img v-lazy="item.picUrl" width="100%" alt="img" @click="goArtistDetail(item.id)" />
            </div>
            <p class="artist-list-title">{{item.name}}</p>
          </a-col>
        </a-row>
      </div>
    </a-skeleton>

    <a-skeleton active :loading="loading">
      <div class="artist-list">
        <div
          style="text-align: left;
          width: 100%;
          font-size: 24px;
          line-height: 1.5em;
          border-bottom: 1px solid #dddddd;
          margin-bottom: 16px;"
        >
          <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
            <use xlink:href="#icon-circle" />
          </svg>热门歌手
        </div>
        <a-row type="flex" justify="space-around">
          <a-col
            :span="4"
            style="margin:0 2px 16px 0"
            class="artist-list-item"
            v-for="(item,index) in hotSinger"
            :key="index"
          >
            <div class="img-box">
              <img v-lazy="item.picUrl" width="100%" alt="img" @click="goArtistDetail(item.id)" />
            </div>
            <p class="artist-list-title">{{item.name}}</p>
          </a-col>
        </a-row>
      </div>
    </a-skeleton>
  </div>
</template>

<script>
import { getArtistList, getTopArtists } from "@/api/artist";
export default {
  name: "",
  props: [""],
  data() {
    return {
      residentSinger: [],
      hotSinger: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getResidentSinger();
    await this.getHotSinger();
    this.loading = false;
  },

  methods: {
    async getResidentSinger() {
      let residentSinger = await getArtistList({
        cat: 5001,
        limit: 10,
        offset: 0
      });
      this.residentSinger = residentSinger.artists.map(item => {
        return {
          id: item.id,
          picUrl: item.picUrl,
          name: item.name
        };
      });
    },
    async getHotSinger() {
      let hotSinger = await getTopArtists({ limit: 20, offset: 0 });
      this.hotSinger = hotSinger.artists.map(item => {
        return { id: item.id, name: item.name, picUrl: item.picUrl };
      });
    },
    goArtistDetail(id) {
      this.$router.push({
        path: "/artist-detail",
        query: {
          id: id
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.artist {
  padding: 36px 16px 100px 16px;
  & .artist-list {
    font-size: 16px;
  }
  & .artist-list-title {
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
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
}
</style>