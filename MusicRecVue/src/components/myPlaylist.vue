<template>
  <div>
    <a-tooltip placement="left">
      <template slot="title">
        <span>播放列表</span>
      </template>
      <div class="switch-playlist">
        <svg class="icon" aria-hidden="true" style="font-size:36px" @click="showDrawer">
          <use xlink:href="#icon-play-list-line" />
        </svg>
      </div>
    </a-tooltip>
    <div class="player-operation">
      <span>
        <svg class="icon operation" aria-hidden="true" @click="lastSong">
          <use xlink:href="#icon-shangyishou" />
        </svg>
      </span>
      <span>
        <svg class="icon operation" aria-hidden="true" @click="nextSong">
          <use xlink:href="#icon-xiayishou" />
        </svg>
      </span>
    </div>
    <a-drawer
      :title="'播放列表 '+ playlist.length + '首'"
      placement="right"
      :closable="false"
      @close="onClose"
      width="25%"
      :visible="visible"
    >
      <button class="more" @click="clearPlaylist">清空列表</button>
      <a-list itemLayout="horizontal" :dataSource="playlist" :locale="locale">
        <a-list-item
          slot="renderItem"
          slot-scope="item, index"
          style="padding-left: 6px"
          :class="currentIndex==index? 'activeItem' : ''"
          :style="currentIndex==index? 'background: rgba('+item.theme[0]+','+item.theme[1]+','+item.theme[2]+',.3)' : {}"
        >
          <a slot="actions">
            <a-icon
              type="caret-right"
              class="actions-item"
              @click="playSong({song:item,idx:index})"
            />
          </a>
          <a slot="actions" class="actions-item">
            <a-icon type="delete" class="actions-item" @click="deleteSong({song:item,idx:index})" />
          </a>
          <a-list-item-meta :description="item.artist">
            <p slot="title" class="title" @click="goSongDetail(item)">{{item.name}}</p>
            <a-avatar
              slot="avatar"
              class="cover-img"
              :src="item.cover"
              style="cursor:pointer"
              @click="goAlbumDetail(item)"
            />
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-drawer>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";
import Bus from "@/utils/bus.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      visible: false,
      locale: { emptyText: "列表空空如也 o(╥﹏╥)o" }
    };
  },

  components: {},

  computed: {
    ...mapGetters(["playlist", "currentIndex"])
  },

  watch: {},

  beforeMount() {},

  mounted() {},

  methods: {
    ...mapMutations(["DELETE_SONG", "CLEAR_PLAYLIST"]),
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    showDrawer() {
      this.visible = true;
    },
    onClose() {
      this.visible = false;
    },
    playSong(data) {
      this.SET_CURRENT_MUSIC_ACTION(data.song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    },
    deleteSong(data) {
      if (data.idx === 0 && this.playlist.length === 1) {
        this.DELETE_SONG(data.idx);
        Bus.$emit("clear");
        return;
      }
      if (data.idx === this.currentIndex) {
        this.nextSong();
      }
      this.DELETE_SONG(data.idx);
    },
    lastSong() {
      Bus.$emit("lastSong");
    },
    nextSong() {
      Bus.$emit("nextSong");
    },
    clearPlaylist() {
      this.CLEAR_PLAYLIST();
      Bus.$emit("clear");
    },
    goSongDetail(song) {
      if (song.songType === "dj") {
        this.$router.push({
          path: "/dj-detail",
          query: {
            rid: song.artistId
          }
        });
      } else {
        this.$router.push({
          path: "/song-detail",
          query: {
            id: song.id
          }
        });
      }
    },
    goArtistDetail(song) {
      this.$router.push({
        path: "/artist-detail",
        query: {
          id: song.artistId
        }
      });
    },
    goAlbumDetail(song) {
      if (song.songType === "dj") {
        this.$router.push({
          path: "/dj-detail",
          query: {
            rid: song.artistId
          }
        });
      } else {
        this.$router.push({
          path: "/album-detail",
          query: {
            id: song.albumId
          }
        });
      }
    }
  }
};
</script>
<style lang='scss' scoped>
.player-operation {
  position: fixed;
  left: 110px;
  bottom: 24px;
  .operation {
    font-size: 24px;
    margin-right: 6px;
    cursor: pointer;
  }
}
.switch-playlist {
  position: fixed;
  right: 8%;
  bottom: 110px;
  cursor: pointer;
  opacity: 0.5;
  &:hover {
    opacity: 1;
  }
}
.more {
  position: relative;
  top: -16px;
  left: 80%;
  font-size: 14px;
  line-height: 2.5em;
  outline: none;
  border: none;
  text-decoration: underline;
  cursor: pointer;
  background-color: rgba(255, 255, 255, 0);
  &:hover {
    color: blue;
  }
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
.title {
  width: 140px;
  cursor: pointer;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.cover-img {
  width: 46px;
  height: 46px;
}
.activeItem {
  .cover-img {
    transition: all 0.3s ease-in-out;
    transition-delay: 0.3s;
    animation: spinDisc 5s linear infinite;
    &:hover {
      animation-play-state: paused;
    }
  }
}
@keyframes spinDisc {
  100% {
    transform: rotate(1turn);
  }
}
</style>