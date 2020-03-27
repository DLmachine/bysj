<template>
  <div class="detail-container" v-bind:style="fullSceen">
    <div class="detail-header">
      <h1><router-link to="/">Ryan' music</router-link></h1>
    </div>
    <div v-if="MvDetail" class="main clearfix">
        <video autoplay :src="MvDetail.src" controls="controls" width="1200"></video>
    </div>
  </div>
</template>

<script>
import Header from "../components/Header";
import Aplayer from "vue-aplayer";

export default {
  name: "SongListDetail",
  components: {
    Header
  },
  async created() {
    let match = window.location.pathname.split("/");
    let tyep = match[2];
    let id = match[3];
    this.getMV(id);
  },
  data() {
    return {
      MvDetail: null,
      fullSceen: {
        height:
          (document.documentElement.clientHeight ||
            document.body.clientHeight) + "px",
        "overflow-y": "hidden"
      },
      listHeight:
        (document.documentElement.clientHeight || document.body.clientHeight) -
        65 -
        100 +
        "px"
    };
  },
  methods: {
    async getMV(id) {
      let result = await this.$api.getMV(id);
      if (result.code === 200) {
        this.MvDetail = result.data;
      }
    }
  }
};
</script>

<style scoped>
.detail-container {
  background-color: #292a2b;
}
.detail-header h1 {
  margin: 0;
  padding: 10px 0;
  border-bottom: 1px solid #cccccc;
}
.detail-header h1 a {
  color: #ffffff;
}
.detail-header h1 a:hover {
  color: #31c27c;
}
.detail-header {
  color: #ffffff;
  text-align: center;
}
.music-list {
  color: #cccccc;
}
.music-list-item {
  font-size: 16px;
  margin: 15px 0;
  text-align: left;
}
.music-list-item a {
  color: #cccccc;
}
.music-list-item a:hover {
  color: #ffffff;
}
.song-name {
  display: inline-block;
  width: 390px;
}
.song-singer {
  display: inline-block;
  width: 180px;
}
.playTime {
  display: inline-block;
  width: 180px;
}
.lyrics {
  width: 350px;
}
</style>

