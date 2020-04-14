<template>
<div style="padding-bottom: 100px;">
  <a-row class="album-list">
    <a-col :span="14" :offset="5">
      <newest-album></newest-album>
    </a-col>

    <a-col :span="14" :offset="5">
      <top-album></top-album>
    </a-col>
  </a-row>
</div>
</template>

<script>
import newestAlbum from "./components/newestAlbum";
import TopAlbum from "./components/topAlbum";
export default {
  name: "",
  props: [""],
  data() {
    return {};
  },

  components: {
    newestAlbum,
    TopAlbum
  },

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {},

  methods: {}
};
</script>

<style lang="scss">
.album-list {
  font-size: 16px;
  margin-top: 16px;
  height: 100%;

  .album-list-top-title {
    text-align: left;
    width: 100%;
    font-size: 24px;
    line-height: 1.5em;
    border-bottom: 1px solid #dddddd;
    margin-bottom: 16px;
  }

  .album-list-item {
    margin-top: 16px;

    img {
      cursor: pointer;
    }
  }

  .album-list-title {
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
}
</style>
