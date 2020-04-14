<template>
  <div>
    <a-back-top style="bottom: 100px;left:10%" />
    <a-row>
      <a-col :span="14" :offset="5">
        <song-info></song-info>
      </a-col>
      <br>
      <a-col :span="10" :offset="5">
        <song-comment></song-comment>
      </a-col>
      <a-col :span="4" :offset="1">
        <similar-song></similar-song>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import SongInfo from "./components/songInfo";
import SongComment from "./components/songComment";
import SimilarSong from "./components/similarSong"
export default {
  name: "",
  props: [""],
  data() {
    return {
      
    };
  },

  components: {
    SongInfo,
    SongComment,
    SimilarSong
  },

  computed: {},

  watch: {
    

  },

  beforeMount() {},

  mounted() {},

  methods: {}
};
</script>
<style lang='scss' scoped>
</style>