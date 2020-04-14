<template>
  <div>
    <div class="song-detail">
      <a-row>
        <a-col :span="5">
          <div class="img-box">
            <img v-lazy="songInfo.cover" class="album-cover" alt="歌曲" />
          </div>
        </a-col>
        <a-col :span="18" :offset="1">
          <div style="margin-top:46px">
            <svg class="icon" aria-hidden="true" style="font-size:46px; margin-right:16px;">
              <use xlink:href="#icon-song-red" />
            </svg>
            <h1>{{songInfo.name}}</h1>
          </div>

          <div class="song-artist">
            <span style="cursor:pointer">
              歌手：
              <span
                style="cursor:pointer"
                v-for="(ar,idx) in songInfo.artists"
                :key="idx"
                @click="goArtistDetail(songInfo.artistId[idx])"
              >
                {{ar}}
                <span v-show="idx !== songInfo.artists.length -1">/</span>
              </span>
            </span>
            <a-button @click.once="playMusic" style="margin-left: 20px">
              <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
                <use xlink:href="#icon-play1" />
              </svg>播放
            </a-button>
            <a-button @click.once="addMusic" style="margin-left: 20px">
              <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
                <use xlink:href="#icon-add" />
              </svg>添加到列表
            </a-button>
          </div>
          <div :class="!expand ? 'album-detail-info' : ''">
            <div>
              <span style="cursor:pointer" @click="goAlbumDetail">专辑：{{songInfo.albumName}}</span>
              <button class="more" @click="showMore">{{expandText}}</button>
            </div>
            <br />
            <p>歌词：</p>
            <pre>{{lyric}}</pre>
          </div>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
import { getSongDetail, getLyric } from "@/api/song.js";
import Bus from "@/utils/bus.js";
import { mapActions } from "vuex";
export default {
  name: "",
  props: [""],
  data() {
    return {
      songInfo: {
        id: null,
        name: "",
        artist: "",
        artists: [],
        artistId: [],
        cover: "",
        albumName: "",
        albumId: null,
        theme: [255, 255, 255]
      },
      lyric: "",
      expand: false,
      expandText: "展开"
    };
  },

  components: {},

  computed: {},

  watch: {
    $route(to, from) {
      this.getSongDetail(to.query.id);
      this.getLyric(to.query.id);
    }
  },

  beforeMount() {},

  async mounted() {
    await this.getSongDetail(this.$route.query.id);
    await this.getLyric(this.$route.query.id);
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getSongDetail(data) {
      let res = await getSongDetail(data);
      let song = res.songs[0];
      let artist = [];
      let artistId = song.ar.map(a => {
        return a.id;
      });
      for (const ar of song.ar) {
        artist.push(ar.name);
      }
      this.songInfo.id = song.id;
      this.songInfo.name = song.name;
      this.songInfo.artist = artist.join("/");
      this.songInfo.artists = artist;
      this.songInfo.artistId = artistId;
      this.songInfo.cover = song.al.picUrl;
      this.songInfo.albumName = song.al.name;
      this.songInfo.albumId = song.al.id;
    },
    async getLyric(data) {
      let res = await getLyric(data);
      this.lyric = res.lrc.lyric.replace(/[\[d{2}:d{2}\.\d{3}\]]/g, "");
    },
    async playMusic() {
      this.SET_CURRENT_MUSIC_ACTION(this.songInfo)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    },
    addMusic() {
      Bus.$emit("add", { list: [this.songInfo], type: "playlist" });
      this.$message.success("已加入播放列表！");
    },
    goArtistDetail(data) {
      this.$router.push({
        path: "/artist-detail",
        query: {
          id: data
        }
      });
    },
    goAlbumDetail() {
      this.$router.push({
        path: "/album-detail",
        query: {
          id: this.songInfo.albumId
        }
      });
    },
    showMore() {
      if (this.expand) {
        this.expand = false;
        this.expandText = "展开";
      } else {
        this.expand = true;
        this.expandText = "收起";
      }
    }
  }
};
</script>
<style lang='scss' scoped>
.song-detail {
  font-size: 14px;
  text-align: left;
  margin-top: 16px;
  .album-cover {
    width: 100%;
    height: 100%;
    margin-top: 30px;
    border-radius: 50%;
  }
  h1 {
    font-size: 24px;
    display: inline;
    position: relative;
    top: -10px;
  }
  .song-artist {
    font-size: 14px;
    line-height: 3em;
    height: 40px;
    margin: 16px 0;
  }
}
.album-detail-info {
  height: 150px;
  overflow: hidden;
}
.more {
  position: absolute;
  bottom: -16px;
  right: 0;
  font-size: 14px;
  line-height: 2.5em;
  outline: none;
  border: none;
  text-decoration: underline;
  cursor: pointer;
  color: blueviolet;
  background-color: rgba(255, 255, 255, 0);
}
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