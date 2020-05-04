<template>
  <div>
    <a-row class="ranking-list">
      <a-col :span="14" :offset="5">
        <a-skeleton active :loading="loading">
          <a-row type="flex" justify="space-around">
              <a-col :span="5" class="ranking-list-item" v-for="(item,index) in coverImgUrl" :key="index">
                <img v-lazy="item.url" width="100%" alt="img" @click="goRankingDetail(index)" />
                <p class="ranking-list-title">{{item.name}}</p>
              </a-col>
          </a-row>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getCoverImgUrl } from "@/api/rankingList.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      coverImgUrl: [],
      loading: true
    };
  },

  components: {
  },

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {
    this.coverImgUrl = getCoverImgUrl();
    this.loading = false;
  },

  methods: {
    goRankingDetail(idx){
      this.$router.push({
        path: '/ranking-detail',
        query: {
          idx: idx
        }
      })
    }
  }
};
</script>
<style lang='scss' scoped>
.ranking-list{
  font-size: 16px;
  margin-top: 16px;
  padding-bottom: 100px;
  .ranking-list-item{
    margin-top: 16px;
    img{
      cursor: pointer;
    }
  }
  .ranking-list-title{
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
}
</style>