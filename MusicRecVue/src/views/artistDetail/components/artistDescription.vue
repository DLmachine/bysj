<template>
  <div>
    <h1>{{artistName}}简介</h1>
    <p>{{artistDesc.briefDesc}}</p>
    <div v-for="(item,index) in artistDesc.introduction" :key="index" class="desc-item">
      <h1>{{item.ti}}</h1>
      <p style="white-space: pre-wrap;">{{item.txt}}</p>
    </div>
  </div>
</template>

<script>
import { getArtistDesc } from "@/api/artist.js";
export default {
  name: "",
  props: ["artistName"],
  data() {
    return {
      artistDesc: {}
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getDesc();
  },

  methods: {
    async getDesc() {
      this.artistDesc = await getArtistDesc(this.$route.query.id);
    }
  }
};
</script>
<style lang='scss' scoped>
h1 {
  font-size: 16px;
  font-weight: bold;
  line-height: 2em;
}
.desc-item {
  margin: 24px 0;
  p {
    line-height: 1.5em;
  }
}
</style>