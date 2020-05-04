<template>
  <div>
    <a-row class="search-container">
      <a-col :span="14" :offset="5">
        <search-bar @search="search"></search-bar>
      </a-col>
      <a-col :span="14" :offset="5">
        <a-tabs defaultActiveKey="1">
          <a-tab-pane key="1">
            <span slot="tab" >歌曲</span>
            <song-result :keywords="keywords"></song-result>
          </a-tab-pane>
          <a-tab-pane key="2">
            <span slot="tab">歌手</span>
            <artist-result :keywords="keywords"></artist-result>
          </a-tab-pane>
          <a-tab-pane key="3">
            <span slot="tab">专辑</span>
            <album-result :keywords="keywords"></album-result>
          </a-tab-pane>
          <a-tab-pane key="4">
            <span slot="tab">歌单</span>
            <playlist-result :keywords="keywords"></playlist-result>
          </a-tab-pane>
          <a-tab-pane key="5">
            <span slot="tab">MV</span>
            <mv-result :keywords="keywords"></mv-result>
          </a-tab-pane>
          <a-tab-pane key="6">
            <span slot="tab">视频</span>
            <video-result :keywords="keywords"></video-result>
          </a-tab-pane>
          <a-tab-pane key="7">
            <span slot="tab">主播电台</span>
            <program-result :keywords="keywords"></program-result>
          </a-tab-pane>
        </a-tabs>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import SearchBar from "./components/searchBar";
import AlbumResult from "./components/albumResult";
import ArtistResult from "./components/artistResult";
import MvResult from "./components/mvResult";
import PlaylistResult from "./components/playlistResult";
import SongResult from "./components/songResult";
import ProgramResult from "./components/programResult";
import VideoResult from "./components/videoResult";
export default {
  name: "search",
  props: [""],
  data() {
    return {
      keywords: ""
    };
  },

  components: {
    SearchBar,
    AlbumResult,
    ArtistResult,
    MvResult,
    PlaylistResult,
    SongResult,
    ProgramResult,
    VideoResult
  },

  methods: {
    search(data){
      this.keywords = data;
    }
  }
};
</script>
<style lang='scss' scoped>
.search-container {
  min-height: 800px;
}
</style>