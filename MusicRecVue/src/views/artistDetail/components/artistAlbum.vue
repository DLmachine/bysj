<template>
  <a-skeleton active :loading="loading">
    <div class="album-list">
      <a-row type="flex" justify="start">
        <a-col
          :span="5"
          style="margin:16px"
          class="album-list-item"
          v-for="(item,index) in albums"
          :key="index"
        >
          <div class="img-box">
            <img
              v-lazy="item.picUrl"
              width="100%"
              alt="img"
              style="cursor:pointer"
              @click="goAlbumDetail(item.id)"
            />
          </div>
          <p class="album-list-title">{{item.name}}</p>
          <p class="album-list-title">{{item.publishTime}}</p>
        </a-col>
      </a-row>
      <a-row type="flex" justify="space-around">
        <a-col>
          <a-pagination
            @change="onChangePage"
            :current="currentPage"
            :total="albumSize"
            :defaultPageSize="20"
            style="margin-top:10px"
          />
        </a-col>
      </a-row>
    </div>
  </a-skeleton>
</template>

<script>
import { getArtistAlbum } from "@/api/artist.js";
import { formatTime } from "@/utils/index";
export default {
  name: "",
  props: ["albumSize"],
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

  async mounted() {
    await this.getAlbums();
    this.loading = false;
  },

  methods: {
    async getAlbums() {
      let res = await getArtistAlbum({
        id: this.$route.query.id,
        limit: 20,
        offset: (this.currentPage - 1) * 20
      });
      this.albums = res.hotAlbums.map(item => {
        return {
          id: item.id,
          name: item.name,
          publishTime: formatTime(item.publishTime, "{y}-{m}-{d}"),
          picUrl: item.picUrl
        };
      });
    },
    async onChangePage(cur) {
      this.currentPage = cur;
      this.loading = true;
      await this.getAlbums();
      this.loading = false;
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