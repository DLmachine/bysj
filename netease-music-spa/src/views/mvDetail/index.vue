<template>
  <div class="mv">
    <a-back-top style="bottom: 100px;left:10%" />
    <a-row>
      <a-col :span="12" :offset="6">
        <mv-detail></mv-detail>
      </a-col>
      <a-col :span="12" :offset="6">
        <mv-comment></mv-comment>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import MvDetail from "./components/mvDetail"
import MvComment from "./components/mvComment";
export default {
  name: "",
  props: [""],
  data() {
    return {};
  },

  components: {
    MvDetail,
    MvComment
  },

  computed: {},

  watch: {},

  beforeMount() {},

  methods: {}
};
</script>
<style lang='scss' scoped>
</style>