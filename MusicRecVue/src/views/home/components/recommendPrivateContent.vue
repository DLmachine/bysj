<template>
  <a-skeleton active :loading="loading">
    <div class="recommend-item">
      <div>
        <svg class="icon" aria-hidden="true" style="font-size:16px;margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>独家放送
      </div>
      <a-row type="flex" justify="space-around" style="padding: 14px 0 0 0">
        <a-col
          :span="7"
          v-for="(item,index) in personalizedPrivateContent"
          :key="index"
          style="margin-bottom: 16px"
        >
          <img v-lazy="item.picUrl" alt="img" width="100%" style="cursor: pointer;" />
          <p class="recommend-title">{{item.name}}</p>
        </a-col>
      </a-row>
    </div>
  </a-skeleton>
</template>

<script>
import {
  getPersonalizedPrivateContent
} from "@/api/home.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      personalizedPrivateContent: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    let personalizedPrivateContent = await getPersonalizedPrivateContent();
    this.personalizedPrivateContent = personalizedPrivateContent.result;
    this.loading = false;
  },

  methods: {}
};
</script>
<style lang='scss' scoped>
</style>