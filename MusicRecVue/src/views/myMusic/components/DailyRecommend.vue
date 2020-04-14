<template>
  <div class="playlist-detail-container">
    <a-row>
      <a-col :span="24" style="margin-top:52px">
        <div class="list-title">
          <span class="title">每日推荐歌曲</span>
          <a-button @click="addMusicList" style="margin-left: 20px">
            <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
              <use xlink:href="#icon-play1" />
            </svg>加入播放列表
          </a-button>
        </div>
        <hr />
        <a-table :dataSource="dailySongs" :pagination="false" :loading="loading">
          <a-table-column title key="action" width="15%" align="center">
            <template slot-scope="text, record">
              <span>
                <svg class="icon play-icon" aria-hidden="true" @click.once="playMusic(record)">
                  <use xlink:href="#icon-play1" />
                </svg>
                <svg class="icon play-icon" aria-hidden="true" @click.once="addMusic(record)">
                  <use xlink:href="#icon-add" />
                </svg>
              </span>
            </template>
          </a-table-column>
          <a-table-column title="歌曲标题" width="35%" key="name">
            <template slot-scope="text, record">
              <a-popover placement="top">
                <template slot="content">
                  <span>{{record.name}}</span>
                </template>
                <span @click="goSongDetail(record)" style="cursor:pointer">{{record.name}}</span>
              </a-popover>
            </template>
          </a-table-column>
          <a-table-column title="歌手" align="center" width="25%" key="artist">
            <template slot-scope="text, record">
              <a-popover placement="top">
                <template slot="content">
                  <span
                    style="cursor:pointer"
                    v-for="(ar,idx) in record.artists"
                    :key="idx"
                    @click="goArtistDetail(record.artistId[idx])"
                  >
                    {{ar}}
                    <span v-show="idx !== record.artists.length -1">/</span>
                  </span>
                </template>
                <span>{{record.artist}}</span>
              </a-popover>
            </template>
          </a-table-column>
          <a-table-column title="专辑" key="albumName">
            <template slot-scope="text, record">
              <a-popover placement="top">
                <template slot="content">
                  <span>{{record.albumName}}</span>
                </template>
                <span @click="goAlbumDetail(record)" style="cursor:pointer">{{record.albumName}}</span>
              </a-popover>
            </template>
          </a-table-column>
        </a-table>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getRecommendSongs } from "@/api/song";
import Bus from "@/utils/bus.js";
import { mapActions } from "vuex";
export default {
  name: "",
  props: [""],
  data() {
    return {
      dailySongs: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getRecommendSongs();
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getRecommendSongs() {
      let res = await getRecommendSongs();
      this.dailySongs = res.recommend.map(item => {
        let artist = [];
        let artistId = item.artists.map(a => {
          return a.id;
        });
        for (const ar of item.artists) {
          artist.push(ar.name);
        }
        return {
          name: item.name,
          id: item.id,
          artist: artist.join("/"),
          artists: artist,
          artistId: artistId,
          cover: item.album.picUrl,
          albumName: item.album.name,
          albumId: item.album.id,
          key: item.id,
          theme: [255, 255, 255]
        };
      });
    },
    addMusicList() {
      Bus.$emit("add", { list: this.dailySongs, type: "playlist" });
      this.$message.success("已加入播放列表！");
    },
    async playMusic(song) {
      this.SET_CURRENT_MUSIC_ACTION(song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    },
    addMusic(song){
      Bus.$emit("add", { list: [song], type: "playlist" });
      this.$message.success("已加入播放列表！");
    },
    goSongDetail(data) {
      this.$router.push({
        path: "/song-detail",
        query: {
          id: data.id
        }
      });
    },
    goAlbumDetail(data) {
      this.$router.push({
        path: "/album-detail",
        query: {
          id: data.albumId
        }
      });
    },
    goArtistDetail(data) {
      this.$router.push({
        path: "/artist-detail",
        query: {
          id: data
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.playlist-detail-container {
  padding: 0 0 100px 16px;
  font-size: 14px;
  .play-icon {
    font-size: 20px;
    cursor: pointer;
  }
  .list-title {
    text-align: left;
    margin-bottom: 10px;
    & > span {
      margin: 10px;
    }
  }
}
.title {
  text-align: left;
  font-size: 16px;
  font-weight: bold;
}
</style>