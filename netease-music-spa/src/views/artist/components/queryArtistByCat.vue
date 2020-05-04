<template>
  <div class="query-artist">
    <a-row type="flex" justify="space-around">
      <a-col
        :span="4"
        style="margin:0 2px 16px 0"
        class="artist-list-item"
        v-for="(item,index) in artistList"
        :key="index"
      >
        <div class="img-box">
          <img v-lazy="item.picUrl" width="100%" alt="img" @click="goArtistDetail(item.id)" />
        </div>
        <p class="artist-list-title">{{item.name}}</p>
      </a-col>
    </a-row>
    <a-row type="flex" justify="space-around">
      <a-col>
        <a-button @click="previous">&lt;</a-button>
        <a-button @click="next">&gt;</a-button>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getArtistList } from "@/api/artist";

export default {
  name: "",
  props: ["artistList"],
  data() {
    return {
      currentPage: 1
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    // await this.getArtists();
  },

  methods: {
    async getArtists() {
      let res = await getArtistList({
        cat: this.$route.query.cat,
        limit: 40,
        offset: (this.currentPage - 1) * 20
      });
      this.artistList = res.artists.map(item => {
        return {
          id: item.id,
          picUrl: item.picUrl,
          name: item.name
        };
      });
    },
    async previous() {
      if (this.currentPage === 1) {
        return;
      } else {
        this.currentPage -= 1;
        await this.getArtists();
      }
    },
    async next() {
      try {
        this.currentPage += 1;
        await this.getArtists();
      } catch(err) {
        this.$message.error("没有更多了...");
      }
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
.query-artist {
  padding: 36px 16px 100px 16px;
  & .artist-list {
    font-size: 16px;
  }
  & .artist-list-title {
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
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
</style>