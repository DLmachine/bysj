<template>
  <div>
    <div class="album-list">
      <div class="album-list-top-title">
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>最新专辑
      </div>
      <a-skeleton active :loading="loading">
        <a-row type="flex" justify="space-around">
          <a-col
            :span="5"
            style="margin:16px"
            class="album-list-item"
            v-for="(item,index) in albums"
            :key="index"
            @click="goAlbumDetail(item.id)"
          >
            <img v-lazy="item.picUrl" width="100%" alt="img" />
            <p class="album-list-title">{{item.name}}</p>
          </a-col>
        </a-row>
      </a-skeleton>
    </div>
  </div>
</template>

<script>
import { getAlbumNewest } from "@/api/album.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      albums: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {
    this.getAlbums();
    this.loading = false;
  },

  methods: {
    async getAlbums() {
      let albums = await getAlbumNewest();
      this.albums = albums.albums.map(item => {
        return {
          id: item.id,
          name: item.name,
          picUrl: item.picUrl
        };
      });
    },
    goAlbumDetail(id) {
      this.$router.push({
        path: "/album-detail",
        query: {
          id: id
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
</style>