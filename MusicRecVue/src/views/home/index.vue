<template>
  <div>
    <a-back-top style="bottom: 100px;left:10%" />
    <banner></banner>
    <recommend></recommend>
    <a-row>
      <a-col :span="24" style="margin-top:-80px;padding-bottom: 100px;">
        <router-link to="/copyright">免责声明</router-link>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import Banner from "@/components/banner.vue";
import Recommend from "./components/recommend.vue"
var _this = this;
export default {
  name: "",
  props: [""],
  data() {
    return {};
  },

  components: {
    Banner,
    Recommend
  },

  computed: {},

  watch: {},

  methods: {}
};
</script>
<style lang='scss' scoped>

</style>