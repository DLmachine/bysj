<template>
  <div>
    <a-row class="dj-list">
      <a-col :span="14" :offset="5">
        <dj-cate></dj-cate>
      </a-col>

      <a-col :span="14" :offset="5">
        <recommend-program></recommend-program>
      </a-col>

      <a-col :span="14" :offset="5">
        <dj-recommend></dj-recommend>
      </a-col>

      <a-col :span="14" :offset="5">
        <today-dj></today-dj>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import DjCate from "./components/djCate"
import RecommendProgram from "./components/recommendProgram"
import TodayDj from "./components/todayDj"
import DjRecommend from "./components/djRecommend"
export default {
  name: "",
  props: [""],
  data() {
    return {
    };
  },

  components: {
    TodayDj,
    RecommendProgram,
    DjRecommend,
    DjCate
  },

  computed: {},

  watch: {},

  beforeMount() {},

  mounted(){

  },

  methods: {
    
  }
};
</script>
<style lang='scss'>
.dj-list {
  font-size: 16px;
  margin-top: 16px;
  height: 100%;
  .dj-list-top-title {
    text-align: left;
    width: 100%;
    font-size: 24px;
    line-height: 1.5em;
    border-bottom: 1px solid #dddddd;
    margin-bottom: 16px;
  }
  .dj-list-item {
    margin-top: 16px;
    img {
      cursor: pointer;
    }
  }
  .dj-list-title {
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
}
</style>