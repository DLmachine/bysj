<template>
  <div style="padding-bottom:100px;">
    <a-back-top style="bottom: 100px;left:10%" />
    <a-skeleton active :loading="loading" v-show="exactSearch.length >0">
      <a-row type="flex" justify="start" style="margin:16px 0">
        <a-col
          :span="4"
          :offset="1"
          v-for="(ar,idx) in exactSearch"
          :key="idx"
          style="margin-bottom:16px"
        >
          <div class="img-box">
            <img v-lazy="ar.coverImgUrl" width="100%" alt="img" @click="goPlaylistDetail(ar.id)" />
          </div>
          <p class="artist-list-title">{{ar.name}}</p>
        </a-col>
      </a-row>
    </a-skeleton>
  </div>
</template>

<script>
import { search } from "@/api/search";
export default {
  name: "",
  props: ["keywords"],
  data() {
    return {
      exactSearch: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {
    async keywords(val) {
      if (val !== "") {
        this.loading = true;
        await this.search(val);
        this.loading = false;
      }
    }
  },

  beforeMount() {},

  async mounted() {
    if (this.keywords !== "") {
      this.loading = true;
      await this.search(this.keywords);
      this.loading = false;
    }
  },

  methods: {
    goPlaylistDetail(id) {
      this.$router.push({
        path: "/playlist-detail",
        query: {
          id: id
        }
      });
    },
    async search(data) {
      let res = await search({ keywords: data, type: 1000 });
      this.exactSearch = res.result.playlists;
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
.artist-list-title {
  font-size: 14px;
  cursor: pointer;
  line-height: 1.5em;
}
</style>