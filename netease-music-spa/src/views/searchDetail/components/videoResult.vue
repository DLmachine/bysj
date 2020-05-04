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
            <img v-lazy="ar.coverUrl" width="100%" alt="img" @click="goMvDetail(ar.vid)" />
          </div>
          <p class="artist-list-title">{{ar.title}}</p>
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
        let res = await search({ keywords: val, type: 1014 });
        this.exactSearch = res.result.videos;
        this.loading = false;
      }
    }
  },

  beforeMount() {},

  async mounted() {
    if (this.keywords !== "") {
      this.loading = true;
      let res = await search({ keywords: this.keywords, type: 1014 });
      this.exactSearch = res.result.videos;
      this.loading = false;
    }
  },

  methods: {
    goMvDetail(id) {
      this.$router.push({
        path: "/mv-detail",
        query: {
          id: id,
          type: "video"
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
img {
  cursor: pointer;
}
</style>