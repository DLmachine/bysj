<template>
  <div>
    <a-row>
      <a-col :span="12" :offset="6" class="artist-detail">
        <a-skeleton active :loading="loading">
          <div>
            <a-row>
              <a-col :span="5">
                <div class="artist-detail-pic-box">
                  <img v-lazy="artist.img1v1Url" alt="artist" class="artist-detail-pic" />
                </div>
              </a-col>
              <a-col span="18" :offset="1">
                <div>
                  <svg
                    class="icon"
                    aria-hidden="true"
                    style="font-size:100px; margin: -26px 26px 0 0;"
                  >
                    <use xlink:href="#icon-singer-copy" />
                  </svg>
                  <h3>{{artist.name}}</h3>
                  <p>
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-song" />
                    </svg>
                    单曲数：{{artist.musicSize}}
                  </p>
                  <p>
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-album" />
                    </svg>
                    专辑数：{{artist.albumSize}}
                  </p>
                  <p>
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-mv" />
                    </svg>
                    mv数：{{artist.mvSize}}
                  </p>
                </div>
              </a-col>
            </a-row>
            <a-row type="flex" justify="space-between" class="tab-option">
              <a-col
                :span="5"
                class="tab-option-item"
                :class="tabIndex ===1 ? 'tab-option-item-active' : ''"
                @click="clickTab(1)"
              >热门单曲(TOP50)</a-col>
              <a-col
                :span="5"
                class="tab-option-item"
                :class="tabIndex ===2 ? 'tab-option-item-active' : ''"
                @click="clickTab(2)"
              >所有专辑</a-col>
              <a-col
                :span="5"
                class="tab-option-item"
                :class="tabIndex ===3 ? 'tab-option-item-active' : ''"
                @click="clickTab(3)"
              >MV</a-col>
              <a-col
                :span="5"
                class="tab-option-item"
                :class="tabIndex ===4 ? 'tab-option-item-active' : ''"
                @click="clickTab(4)"
              >艺人介绍</a-col>
            </a-row>
            <a-row style="margin-top:16px">
              <a-col span="24">
                <hot-song v-if="tabIndex === 1" :hotSongs="hotSongs"></hot-song>
                <artist-album v-if="tabIndex === 2" :albumSize="artist.albumSize"></artist-album>
                <artist-mv v-if="tabIndex === 3" ></artist-mv>
                <artist-description v-if="tabIndex === 4" :artistName="artist.name"></artist-description>
              </a-col>
            </a-row>
          </div>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import HotSong from "./components/hotSong.vue";
import ArtistAlbum from "./components/artistAlbum.vue"
import ArtistMv from "./components/artistMv.vue"
import ArtistDescription from "./components/artistDescription.vue"
import { getArtist } from "@/api/artist.js";

export default {
  name: "",
  props: [""],
  data() {
    return {
      loading: true,
      tabIndex: 1,
      artist: {},
      hotSongs: []
    };
  },

  components: {
    HotSong,
    ArtistAlbum,
    ArtistMv,
    ArtistDescription
  },

  computed: {},

  watch: {
    $route(to, from) {
      this.getArtistInfo();
    }
  },

  beforeMount() {},

  async mounted() {
    await this.getArtistInfo();
    this.loading = false;
  },

  methods: {
    async getArtistInfo() {
      let res = await getArtist(this.$route.query.id);
      this.artist = res.artist;
      /* 格式化热门歌曲 */
      this.hotSongs = res.hotSongs.map(item => {
        let artist = [];
        let artistId = item.ar.map(a=>{
          return a.id
        });
        for (const ar of item.ar) {
          artist.push(ar.name);
        }
        return {
          name: item.name,
          id: item.id,
          artist: artist.join("/"),
          artists: artist,
          artistId: artistId,
          cover: item.al.picUrl,
          albumName: item.al.name,
          albumId: item.al.id,
          pop: item.pop,
          key: item.id,
          theme: [255,255,255]
        };
      });
    },
    clickTab(idx){
      if (idx === this.tabIndex){
        return
      } else {
        this.tabIndex = idx;
      }
    }
  }
};
</script>
<style lang='scss' scoped>
.artist-detail {
  padding: 16px 16px 100px 16px;
  margin-top: 16px;
  text-align: left;
  font-size: 14px;
  h3 {
    display: inline;
    font-size: 24px;
    position: relative;
    top: -24px;
  }
  .artist-detail-pic-box {
    margin-top: 6px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    .artist-detail-pic {
      width: 100%;
      height: auto;
    }
  }
  .tab-option {
    border-bottom: 1px solid #ccc;
    margin-top: 16px;
    .tab-option-item {
      font-size: 16px;
      line-height: 2em;
      text-align: center;
      cursor: pointer;
    }
    .tab-option-item-active {
      border-bottom: 2px solid #d81e06;
    }
  }
}
</style>