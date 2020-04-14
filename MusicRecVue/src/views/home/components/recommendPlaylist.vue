<template>
  <a-skeleton active :loading="loading">
    <div class="recommend-item">
      <div>
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>推荐歌单
      </div>
      <a-row type="flex" justify="space-between" style="padding: 14px 0 0 0;overflow:hidden;">
        <a-col
          :span="4"
          v-for="(item,index) in personalized"
          :key="index"
          style="margin:0 2px 16px 0;"
          @click="goPlaylistDetail(item.id)"
        >
          <div class="img-box">
            <img v-lazy="item.picUrl" alt="img" />
          </div>
          <div style="height:46px;overflow:hidden">
            <p class="recommend-title">{{item.name}}</p>
          </div>
        </a-col>
      </a-row>
    </div>
  </a-skeleton>
</template>

<script>
import { getPersonalized } from "@/api/home.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      personalized: [],
      playlist: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    let personalized = await getPersonalized();
    this.personalized = personalized.result;
    this.loading = false;
  },

  methods: {
    goPlaylistDetail(id){
      this.$router.push({
        path: '/playlist-detail',
        query: {
          id: id
        }
      })
    }
  }
};
</script>
<style lang='scss' scoped>
</style>