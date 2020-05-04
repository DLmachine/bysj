<template>
  <div class="playlist-detail-container">
    <a-row>
      <a-col>
        <div class="playlist-detail">
          <a-row>
            <a-col :span="5">
              <img v-lazy="playList.picUrl" width="100%" style="margin-top:30px" alt="歌单" />
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
                <a-button @click="addMusicList" style="margin-right: 20px">
                  <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
                    <use xlink:href="#icon-play1" />
                  </svg>加入播放列表
                </a-button>
                <a-button
                  v-if="showUnsubscribeBtn"
                  @click="unsubscribe(playList.id)"
                  style="margin-right: 20px"
                >
                  <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
                    <use xlink:href="#icon-like1" />
                  </svg>取消收藏
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

        <div>
          <div class="list-title">
            <span style="font-size:24px">歌曲列表</span>
            <span>共{{playList.tracks.length}}首</span>
          </div>
          <a-table :dataSource="playList.tracks" :pagination="pagination">
            <a-table-column title key="action" align="center" width="15%">
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
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { subscribePlaylist } from "@/api/playList.js";
import Bus from "@/utils/bus.js";
import { mapActions } from "vuex";
export default {
  name: "",
  props: ["playList", "showUnsubscribeBtn"],
  data() {
    return {
      pagination: { defaultPageSize: 40 }
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {},

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
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
    async unsubscribe(data) {
      await subscribePlaylist({ id: data, type: 2 });
      this.$message.success("已取消收藏！");
      Bus.$emit("unsubscribe", data);
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
.playlist-detail {
  text-align: left;
  margin-top: 16px;
  padding-bottom: 20px;
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