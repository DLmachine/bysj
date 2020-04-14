<template>
  <a-skeleton active :loading="loading">
    <div class="recommend-item">
      <div>
        <svg class="icon" aria-hidden="true" style="font-size:16px;margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>最新音乐
      </div>
      <a-row type="flex" justify="space-around" style="padding: 14px 0 0 0">
        <a-col :span="12" v-for="(item,index) in personalizedNewSong" :key="index">
          <a-row type="flex" justify="start" class="recommend-new-songs">
            <a-col :span="3" style="position:relative;">
              <div @click.once="addMusic(item)">
                <svg
                  class="icon play"
                  aria-hidden="true"
                  style="font-size:16px; margin-right:16px;"
                >
                  <use xlink:href="#icon-play" />
                </svg>
                <img
                  v-lazy="item.cover"
                  width="100%"
                  alt="img"
                  style="margin:9px 0 0 9px;cursor: pointer;z-index:-1"
                />
              </div>
            </a-col>
            <a-col :span="18" :offset="1">
              <p
                class="recommend-title"
                style="line-height:1.5em;cursor:pointer"
                @click="goSongDetail(item)"
              >{{item.name}}</p>
              <span
                class="recommend-title"
                style="line-height:1.5em;cursor:pointer;color:#999"
                v-for="(ar,idx) in item.artists"
                :key="idx"
                @click="goArtistDetail(item.artistId[idx])"
              >{{ar}}<span v-show="idx !== item.artists.length -1">/</span></span>
            </a-col>
          </a-row>
        </a-col>
      </a-row>
    </div>
  </a-skeleton>
</template>

<script>
import { getPersonalizedNewSong } from "@/api/home.js";
import Bus from "@/utils/bus.js";
import { mapActions } from "vuex";
export default {
  name: "",
  props: [""],
  data() {
    return {
      personalizedNewSong: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getNewSong();
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getNewSong() {
      let personalizedNewSong = await getPersonalizedNewSong();
      this.personalizedNewSong = personalizedNewSong.result.map(item => {
        let artist = [];
        let artistId = item.song.artists.map(a=>{
          return a.id
        });
        for (const ar of item.song.artists) {
          artist.push(ar.name);
        }
        return {
          name: item.name,
          id: item.id,
          artist: artist.join("/"),
          artists: artist,
          artistId: artistId,
          cover: item.song.album.blurPicUrl,
          albumName: item.song.album.name,
          albumId: item.song.album.id,
          theme: [255, 255, 255]
        };
      });
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
    }
  }
};
</script>
<style lang='scss' scoped>
</style>