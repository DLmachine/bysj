<<<<<<< HEAD
<template>
  <a-skeleton active :loading="loading">
    <div class="recommend-item">
      <div>
        <svg class="icon" aria-hidden="true" style="font-size:16px;margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>推荐MV
      </div>
      <a-row type="flex" justify="space-around" style="padding: 14px 0 0 0">
        <a-col
          :span="5"
          v-for="(item,index) in personalizedMv"
          :key="index"
          style="margin-bottom: 16px"
        >
          <img
            v-lazy="item.picUrl"
            alt="img"
            width="100%"
            style="cursor: pointer;"
            @click="goMvDetail(item.id)"
          />
          <p class="recommend-title">{{item.name}}</p>
        </a-col>
      </a-row>
    </div>
  </a-skeleton>
</template>

<script>
import { getPersonalizedMv } from "@/api/home.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      personalizedMv: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    let personalizedMv = await getPersonalizedMv();
    this.personalizedMv = personalizedMv.result;
    this.loading = false;
  },

  methods: {
    goMvDetail(id) {
      this.$router.push({
        path: "/mv-detail",
        query: {
          id: id,
          type: "mv"
        }
      });
    }
  }
};
</script>