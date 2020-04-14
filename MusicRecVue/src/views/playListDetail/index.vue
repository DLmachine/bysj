<template>
  <div class="playlist-detail-container">
    <a-row>
      <a-col :span="14" :offset="5">
        <a-skeleton active :loading="loading">
          <div class="playlist-detail">
            <a-row>
              <a-col :span="5">
                <img v-lazy="playList.picUrl" style="margin-top:30px" width="100%" alt="歌单" />
              </a-col>
              <a-col :span="18" :offset="1">
                <svg class="icon" aria-hidden="true" style="font-size:100px; margin-right:16px;">
                  <use xlink:href="#icon-qukugedan" />
                </svg>
                <h1>{{playList.name}}</h1>
                <div class="playlist-creator">
                  <img v-lazy="playList.creator.avatarUrl" width="36px" alt />
                  <span>{{playList.creator.nickname}}&nbsp;&nbsp;于&nbsp;&nbsp;{{playList.createTime}}&nbsp;&nbsp;创建</span>
                </div>
                <div>
                  <a-button @click.once="addMusicList" style="margin-right: 20px">
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-play1" />
                    </svg>加入播放列表
                  </a-button>
                  <a-button @click.once="subscribe(playList.id)" style="margin-right: 20px">
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-like2" />
                    </svg>收藏歌单
                  </a-button>
                </div>
                <div class="tag">
                  <span>标签：</span>
                  <a-tag color="pink" v-for="(tag,idx) in playList.tags" :key="idx">{{tag}}</a-tag>
                </div>
                <div>
                  介绍：
                  <p>{{playList.description}}</p>
                </div>
              </a-col>
            </a-row>
          </div>
          <div class="album-tracks"></div>
        </a-skeleton>

        <a-skeleton active :loading="loading">
          <div>
            <div class="list-title">
              <span style="font-size:24px">歌曲列表</span>
              <span>共{{playList.tracks.length}}首</span>
            </div>
            <a-table :dataSource="playList.tracks">
              <a-table-column title align="center" key="action" width="10%">
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
          </div>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getPlaylistDetail, subscribePlaylist } from "@/api/playList.js";
import Bus from "@/utils/bus.js";
import { mapActions } from "vuex";
import { formatTime } from "@/utils/index";
export default {
  name: "",
  props: [""],
  data() {
    return {
      loading: true,
      playList: {
        id: "",
        creator: {},
        createTime: "",
        trackIds: [],
        tracks: [],
        tags: [],
        picUrl: "",
        name: "",
        description: ""
      }
    };
  },

  components: {},

  computed: {},

  watch: {
    $route(to, from) {
      this.getListDetail(this.$route.query.id);
    }
  },

  beforeMount() {},

  async mounted() {
    await this.getListDetail(this.$route.query.id);
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getListDetail(data) {
      //获取歌单信息
      let res = await getPlaylistDetail(data);
      // this.playList = res.playlist;
      this.playList.id = res.playlist.id;
      this.playList.creator = res.playlist.creator;
      this.playList.createTime = formatTime(
        res.playlist.createTime,
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
      this.playList.tags = res.playlist.tags;
      this.playList.picUrl = res.playlist.coverImgUrl;
      this.playList.name = res.playlist.name;
      this.playList.description = res.playlist.description;
    },
    addMusicList() {
      Bus.$emit("add", { list: this.playList.tracks, type: "playlist" });
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
    async subscribe(data) {
      await subscribePlaylist({ id: data, type: 1 });
      this.$message.success("收藏成功！");
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
    goAlbumDetail(song) {
      this.$router.push({
        path: "/album-detail",
        query: {
          id: song.albumId
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.playlist-detail-container {
  padding-bottom: 100px;
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
.playlist-detail {
  text-align: left;
  margin-top: 16px;
  padding-bottom: 30px;
  h1 {
    font-size: 24px;
    display: inline;
    position: relative;
    top: -26px;
  }
  .playlist-creator {
    font-size: 14px;
    line-height: 3em;
    height: 40px;
    margin: -16px 0 16px 0;
    img {
      margin-right: 16px;
      float: left;
      clear: both;
      border-radius: 50%;
    }
  }
  .tag {
    font-size: 14px;
    margin: 14px 0;
  }
}
</style>