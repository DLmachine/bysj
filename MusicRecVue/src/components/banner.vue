<template>
  <div>
    <a-row>
      <a-col :span="14" :offset="5">
        <a-skeleton active :loading="loading">
          <div class="banner">
            <a-carousel effect="fade" autoplay arrows>
              <div
                slot="prevArrow"
                slot-scope="props"
                class="custom-slick-arrow"
                style="left: -50px;zIndex: 1"
              >
                <a-icon type="left-circle" />
              </div>
              <div
                slot="nextArrow"
                slot-scope="props"
                class="custom-slick-arrow"
                style="right: -50px"
              >
                <a-icon type="right-circle" />
              </div>
              <div v-for="(item,index) in banner" :key="index" @click="bannerClick(item)">
                <img :src="item.imageUrl" width="100%" alt="banner" />
                <span
                  class="banner-tag"
                  v-bind:style="'background:'+ item.titleColor"
                >{{item.typeTitle}}</span>
              </div>
            </a-carousel>
          </div>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getBanner } from "@/api/home.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      banner: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    let banner = await getBanner();
    this.banner = banner.banners;
    this.loading = false;
  },

  methods: {
    bannerClick(banner) {
      switch (banner.targetType) {
        case 1:
          this.goSongDetail(banner);
          break;
        case 10:
          this.goAlbumDetail(banner);
          break;
        case 100:
          this.goArtistDetail(banner);
          break;
        case 1000:
          this.goPlaylistDetail(banner);
          break;
        case 1004:
          this.goMvDetail(banner);
          break;
        case 3000:
          window.open(banner.url);
          break;
        default:
          break;
      }
    },
    goSongDetail(song) {
      this.$router.push({
        path: "/song-detail",
        query: {
          id: song.targetId
        }
      });
    },
    goAlbumDetail(album) {
      this.$router.push({
        path: "/album-detail",
        query: {
          id: album.targetId
        }
      });
    },
    goMvDetail(mv) {
      this.$router.push({
        path: "/mv-detail",
        query: {
          id: mv.targetId,
          type: "mv"
        }
      });
    },
    goArtistDetail(ar) {
      this.$router.push({
        path: "/artist-detail",
        query: {
          id: ar.targetId
        }
      });
    },
    goPlaylistDetail(pl) {
      this.$router.push({
        path: "/playlist-detail",
        query: {
          id: pl.targetId
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.ant-carousel >>> .slick-slide {
  text-align: center;
  background: transparent;
  overflow: hidden;
}
.custom-slick-arrow {
  width: 36px !important;
  height: 36px !important;
  font-size: 36px !important;
  color: #242424 !important;
  opacity: 0.3;
  background-color: transparent;
  &::before {
    display: none;
  }
  &:hover {
    color: #c20c0c !important;
    opacity: 1;
  }
}
.banner-tag {
  position: absolute;
  right: 20px;
  bottom: 20px;
  border-radius: 1em;
  padding: 0 6px;
  color: #fff;
}
</style>