<template>
  <div>
    <div class="dj-list">
      <div class="dj-list-top-title">
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>精选电台 - 订阅更精彩
      </div>
      <a-skeleton active :loading="loading">
        <a-row type="flex" justify="space-around">
          <a-col
            :span="4"
            style="margin:0 2px 16px 0"
            class="dj-list-item"
            v-for="(item,index) in djs"
            :key="index"
            @click="goDjDetail(item)"
          >
            <img v-lazy="item.picUrl" width="100%" alt="img" />
            <p class="dj-list-title">{{item.name}}</p>
          </a-col>
        </a-row>
      </a-skeleton>
    </div>
  </div>
</template>

<script>
import { getDjRecommend } from "@/api/dj.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      djs: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getDjs();
    this.loading = false;
  },

  methods: {
    async getDjs() {
      let djs = await getDjRecommend();
      this.djs = djs.djRadios.map(item => {
        return {
          name: item.name,
          id: item.id,
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