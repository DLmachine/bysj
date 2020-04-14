<template>
  <div class="dj-list" style="padding-bottom:100px;">
    <div class="dj-list-top-title">
      <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
        <use xlink:href="#icon-circle" />
      </svg>今日优选
    </div>
    <a-skeleton active :loading="loading">
      <a-row type="flex" justify="space-around">
        <a-col
          :span="4"
          style="margin:0 2px 16px 0"
          class="dj-list-item"
          v-for="(item,index) in todayDj"
          :key="index"
          @click="goDjDetail(item)"
        >
          <img v-lazy="item.picUrl" width="100%" alt="img" />
          <p class="dj-list-title">{{item.name}}</p>
        </a-col>
      </a-row>
    </a-skeleton>
  </div>
</template>

<script>
import { getTodayDj } from "@/api/dj.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      loading: true,
      todayDj: []
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getTodayDj();
    this.loading = false;
  },

  methods: {
    async getTodayDj() {
      let todayDj = await getTodayDj();
      this.todayDj = todayDj.data.map(item => {
        return {
          id: item.id,
          name: item.name,
          picUrl: item.picUrl
        };
      });
    },
    goDjDetail(data) {
      this.$router.push({
        path: "/dj-detail",
        query: {
          rid: data.id
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
</style>