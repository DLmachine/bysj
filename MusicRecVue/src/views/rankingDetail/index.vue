<template>
  <div class="playlist-detail-container">
    <a-row>
      <a-col :span="14" :offset="5">
        <a-skeleton active :loading="loading">
          <div class="playlist-detail">
            <a-row>
              <a-col :span="5">
                <img v-lazy="playList.picUrl" width="100%" alt="歌单" />
              </a-col>
              <a-col :span="18" :offset="1">
                <svg class="icon" aria-hidden="true" style="font-size:36px; margin-right:16px;">
                  <use xlink:href="#icon-paihangbang" />
                </svg>
                <h1>{{playList.name}}</h1>
                <div class="playlist-creator">
                  <img v-lazy="playList.creator.avatarUrl" width="36px" alt />
                  <span>{{playList.creator.nickname}}&nbsp;&nbsp;最近更新&nbsp;&nbsp;{{playList.updateTime}}</span>
                  <a-button @click.once="addMusicList" style="margin-left: 20px">
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-play1" />
                    </svg>加入播放列表
                  </a-button>
                </div>
                <div>
                  介绍：
                  <p>{{playList.description}}</p>
                </div>
              </a-col>
            </a-row>
          </div>
        </a-skeleton>

        <a-skeleton active :loading="loading">
          <div>
            <div class="list-title">
              <span style="font-size:24px">歌曲列表</span>
              <span>共{{playList.tracks.length}}首</span>
            </div>
            <a-table :dataSource="playList.tracks">
              <a-table-column title key="action" width="10%">
                <template slot-scope="text, record">
                  <span>
                    <svg class="icon play-icon" aria-hidden="true" @click.once="addMusic(record)">
                      <use xlink:href="#icon-play1" />
                    </svg>
                  </span>
                </template>
              </a-table-column>
              <a-table-column title="歌曲标题" width="40%" key="title">
                <template slot-scope="text, record">
                  <a-popover placement="top">
                    <template slot="content">
                      <span>{{record.name}}</span>
                    </template>
                    <span @click="goSongDetail(record)" style="cursor:pointer">{{record.name}}</span>
                  </a-popover>
                </template>
              </a-table-column>
              <a-table-column title="歌手" width="25%" key="artist">
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
          </div>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getRankingList } from "@/api/rankingList.js";
import { mapActions } from "vuex";
import Bus from "@/utils/bus.js";
import { formatTime } from "@/utils/index";
export default {
  name: "",
  props: [""],
  data() {
    return {
      playList: {
        id: "",
        creator: {},
        updateTime: "",
        trackIds: [],
        tracks: [],
        picUrl: "",
        name: "",
        description: ""
      },
      loading: true
    };
  },

  components: {},

  computed: {
    idx() {
      return this.$route.query.idx;
    }
  },

  watch: {
    $route(to, from) {
      this.getList();
    }
  },

  beforeMount() {},

  async mounted() {
    await this.getList();
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getList() {
      let res = await getRankingList(this.idx);
      this.playList.id = res.playlist.id;
      this.playList.creator = res.playlist.creator;
      this.playList.updateTime = formatTime(
        res.playlist.updateTime,
        "{y}-{m}-{d}"
      );
      this.playList.trackIds = res.playlist.trackIds;
      this.playList.tracks = res.playlist.tracks.map(item => {
        let artist = [];
        let artistId = item.ar.map(a => {
          return a.id;
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
          key: item.id,
          theme: [255, 255, 255]
        };
      });
      this.playList.picUrl = res.playlist.coverImgUrl;
      this.playList.name = res.playlist.name;
      this.playList.description = res.playlist.description;
    },
    addMusicList() {
      Bus.$emit("add", { list: this.playList.tracks, type: "ranking" });
      this.$message.success("已加入播放列表！");
    },
    async addMusic(song) {
      this.SET_CURRENT_MUSIC_ACTION(song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    },
    goSongDetail(song) {
      this.$router.push({
        path: "/song-detail",
        query: {
          id: song.id
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
    },
    goAlbumDetail(data) {
      this.$router.push({
        path: "/album-detail",
        query: {
          id: data.albumId
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.playlist-detail-container {
  padding-bottom: 100px;
  text-align: left;
  font-size: 14px;
  .play-icon {
    margin-left: 40%;
    font-size: 24px;
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
.playlist-detail {
  text-align: left;
  margin-top: 46px;
  padding-bottom: 100px;
  h1 {
    font-size: 24px;
    display: inline;
    position: relative;
    top: -4px;
  }
  .playlist-creator {
    font-size: 14px;
    line-height: 3em;
    height: 40px;
    margin: 16px 0;
    img {
      margin-right: 16px;
      float: left;
      clear: both;
      border-radius: 50%;
    }
  }
}
</style>