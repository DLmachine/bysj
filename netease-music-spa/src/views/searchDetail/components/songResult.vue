<template>
  <div style="padding-bottom: 100px">
    <a-back-top style="bottom: 100px;left:10%" />
    <a-row>
      <a-col>
        <a-table :dataSource="exactSearch" :loading="loading" v-show="exactSearch.length>0">
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
          <a-table-column title="歌曲标题" width="40%" key="name">
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
import { getSongDetail } from "@/api/song.js";
import { search } from "@/api/search";
import { mapActions } from "vuex";
import Bus from "@/utils/bus.js";
export default {
  name: "",
  props: ["keywords"],
  data() {
    return {
      locale: { emptyText: "" },
      loading: true,
      exactSearch: []
    };
  },

  components: {},

  computed: {},

  watch: {
    async keywords(val) {
      if (val !== "") {
        this.loading = true;
        await this.search(val);
        this.loading = false;
      }
    }
  },

  beforeMount() {},

  async mounted() {
    if (this.keywords !== "") {
      this.loading = true;
      await this.search(this.keywords);
      this.loading = false;
    }
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async search(data) {
      let res = await search({ keywords: data, type: 1 });
      this.exactSearch = res.result.songs.map(item => {
        let artist = [];
        let artistId = item.artists.map(a => {
          return a.id;
        });
        for (const ar of item.artists) {
          artist.push(ar.name);
        }
        return {
          id: item.id,
          name: item.name,
          artist: artist.join("/"),
          artists: artist,
          artistId: artistId,
          cover:
            "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg",
          albumName: item.album.name,
          albumId: item.album.id,
          theme: [255, 255, 255],
          key: item.id
        };
      });
    },
    async playMusic(song) {
      let cover = await this.getCover(song.id);
      song.cover = cover;
      this.SET_CURRENT_MUSIC_ACTION(song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    },
    async addMusic(song){
      let cover = await this.getCover(song.id);
      song.cover = cover;
      Bus.$emit("add", { list: [song], type: "playlist" });
      this.$message.success("已加入播放列表！");
    },
    async getCover(data) {
      let res = await getSongDetail(data);
      let song = res.songs[0];
      return song.al.picUrl;
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
.cover-img {
  width: 46px;
  height: 46px;
}
.actions-item {
  font-size: 16px;
  opacity: 0.8;
  &:hover {
    opacity: 1;
    transition: all 0.1s ease-in-out;
    transform: scale(1.5);
  }
}
.play-icon {
  font-size: 20px;
  cursor: pointer;
}
</style>