<template>
  <div>
    <div class="album-list">
      <div class="album-list-top-title">
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>全部新碟
      </div>
      <a-skeleton active :loading="loading">
        <a-row type="flex" justify="space-around">
          <a-col
            :span="5"
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

    <a-pagination
      @change="onChangePage"
      :current="currentPage"
      :total="50"
      style="margin-top:10px"
    />
  </div>
</template>

<script>
import { getTopAlbum } from "@/api/album.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      albums: [],
      currentPage: 1,
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {
    this.getAlbums({ offset: 0 });
    this.loading = false;
  },

  methods: {
    async getAlbums(data) {
      let albums = await getTopAlbum(data);
      this.albums = albums.albums.map(item => {
        return {
          id: item.id,
          picUrl: item.picUrl,
          name: item.name
        };
      });
    },
    async onChangePage(cur) {
      this.currentPage = cur;
      await this.getAlbums({ offset: (this.currentPage - 1) * 20 });
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