<template>
  <div class="dj-cate">
    <a-row type="flex" justify="start">
      <div class="dj-cate-top-title">
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>电台分类
      </div>
      <a-skeleton active :loading="loading1">
        <div>
          <a-col :span="2" style="margin: 6px 16px" v-for="(cate,index) in cateList" :key="index">
            <img v-lazy="cate.pic56x56Url" width="40%" alt="img" @click="getDjRecommend(cate.id)" />
            <p class="dj-cate-list-title">{{cate.name}}</p>
          </a-col>
        </div>
      </a-skeleton>
    </a-row>
    <a-row type="flex" justify="start" style="padding: 14px 0 0 0" v-if="isShowRecommend">
      <div class="dj-cate-top-title">
        <svg class="icon" aria-hidden="true" style="font-size:16px; margin-right:16px;">
          <use xlink:href="#icon-circle" />
        </svg>分类推荐
        <button class="more" @click="isShowRecommend = false">收起</button>
      </div>
      <a-skeleton active :loading="loading2">
        <div>
          <a-col :span="12" v-for="(item,index) in djRecommend" :key="index">
            <a-row type="flex" justify="start" class="recommend-new-songs">
              <a-col :span="3" style="position:relative;">
                <div @click="goDjDetail(item)">
                  <img
                    v-lazy="item.picUrl"
                    width="100%"
                    alt="img"
                    style="margin:9px 0 0 9px;cursor: pointer;z-index:-1"
                  />
                </div>
              </a-col>
              <a-col :span="18" :offset="1">
                <p class="recommend-title">{{item.name}}</p>
              </a-col>
            </a-row>
          </a-col>
        </div>
      </a-skeleton>
    </a-row>
  </div>
</template>

<script>
import { getDjCateList, getDjRecommendType } from "@/api/dj.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      cateList: [],
      djRecommend: [],
      isShowRecommend: false,
      loading1: true,
      loading2: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getDjCateList();
    this.loading1 = false;
    this.loading2 = false;
  },

  methods: {
    async getDjCateList() {
      let res = await getDjCateList();
      this.cateList = res.categories;
    },
    async getDjRecommend(id) {
      this.isShowRecommend = true;
      this.loading2 = true;
      let res = await getDjRecommendType(id);
      this.djRecommend = res.djRadios;
      this.loading2 = false;
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
.dj-cate {
  padding: 14px 0;
}
.dj-cate-top-title {
  text-align: left;
  width: 100%;
  font-size: 24px;
  line-height: 1.5em;
  border-bottom: 1px solid #dddddd;
  margin-bottom: 16px;
}
.more {
  color: blueviolet;
  float: right;
  font-size: 14px;
  line-height: 2.5em;
  outline: none;
  border: none;
  text-decoration: underline;
  cursor: pointer;
  background-color: rgba(255, 255, 255, 0);
}
.dj-cate-list-title {
  font-size: 12px;
  cursor: text;
  line-height: 1.5em;
}
.recommend-title {
  text-align: left;
  margin-top: 10px;
  font-size: 14px;
  line-height: 2em;
  cursor: text;
}
.recommend-new-songs {
  border-bottom: 1px solid #ddd;
  margin-right: 16px;
}
</style>