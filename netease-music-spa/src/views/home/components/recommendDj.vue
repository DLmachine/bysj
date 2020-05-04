<template>
  <a-skeleton active :loading="loading">
    <div class="recommend-item">
      <div>
        <svg class="icon" aria-hidden="true" style="font-size:16px;margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>电台节目
      </div>
      <a-row type="flex" justify="space-around" style="padding: 14px 0 0 0">
        <a-col
          :span="3"
          v-for="(item,index) in personalizedDJProgram"
          :key="index"
          style="margin-bottom:16px"
        >
          <div class="img-box">
            <img v-lazy="item.cover" alt="img" @click.once="addMusic(item)" />
          </div>
          <p class="recommend-title">{{item.name}}</p>
        </a-col>
      </a-row>
    </div>
  </a-skeleton>
</template>

<script>
import { getPersonalizedDJProgram } from "@/api/home.js";
import { mapActions } from "vuex";
import Bus from "@/utils/bus.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      personalizedDJProgram: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    let personalizedDJProgram = await getPersonalizedDJProgram();
    this.personalizedDJProgram = personalizedDJProgram.result.map(item => {
      return {
        name: item.name,
        id: item.program.mainSong.id,
        artist: item.program.dj.nickname,
        artistId: item.program.radio.id,
        cover: item.picUrl,
        theme: [255, 255, 255],
        songType: "dj"
      };
    });
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async addMusic(song) {
      this.SET_CURRENT_MUSIC_ACTION(song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
<style lang='scss' scoped>
</style>