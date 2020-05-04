<template>
  <div id="aplayer"></div>
</template>

<script>
import { getLyric } from "@/api/song.js";
/* import "APlayer/dist/APlayer.min.css";
import APlayer from "APlayer"; */
import Bus from "@/utils/bus.js";
import { mapMutations, mapActions } from "vuex";
export default {
  name: "",
  props: [""],
  data() {
    return {};
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {
    let options = {
      container: document.getElementById("aplayer"),
      autoplay: true,
      volume: 1,
      loop: 'none',
      lrcType: 2,
      listFolded: true,
      listMaxHeight: "300px",
      theme: "#FFDB00"
    };
    const ap = new APlayer(options);
    ap.on("ended", () => {
      Bus.$emit("nextSong");
    });
    Bus.$on("play", song => {
      ap.list.clear();
      ap.list.add(song);
      ap.list.switch(0);
      ap.play();
    });
    Bus.$on("add", data => {
      this.ADD_PLAYLIST(data.list);
    });
    Bus.$on("lastSong", () => {
      this.LAST_SONG()
        .then(song => {
          ap.list.clear();
          ap.list.add(song);
          ap.list.switch(0);
          ap.play();
        })
        .catch();
    });
    Bus.$on("nextSong", () => {
      this.NEXT_SONG()
        .then(song => {
          ap.list.clear();
          ap.list.add(song);
          ap.list.switch(0);
          ap.play();
        })
        .catch();
    });
    Bus.$on("clear",()=>{
      ap.list.clear();
    })
  },

  methods: {
    ...mapActions(["NEXT_SONG", "LAST_SONG"]),
    ...mapMutations(["ADD_PLAYLIST"])
  }
};
</script>
<style lang='scss' scoped>
#aplayer {
  text-align: left;
}
</style>