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
            <img v-lazy="ar.cover" width="100%" alt="img" @click="goDjDetail(ar.id)" />
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
      loading: true,
      exactSearch: []
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
    async search(data) {
      let res = await search({ keywords: data, type: 1009 });
      this.exactSearch = res.result.djRadios.map(item => {
        return {
          id: item.id,
          name: item.name,
          cover: item.picUrl
        };
      });
    },
    goDjDetail(data) {
      this.$router.push({
        path: "/dj-detail",
        query: {
          rid: data
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
.artist-list-title {
  font-size: 14px;
  cursor: pointer;
  line-height: 1.5em;
}
</style>