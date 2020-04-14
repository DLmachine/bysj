<template>
  <div class="artist-choose">
    <div v-for="(item,index) in categoryList" :key="index" class="artist-category">
      <h3>{{item.title}}</h3>
      <ul>
        <li v-for="(cat,idx) in item.list" :key="idx" @click="queryArtist(cat.cat)">{{cat.name}}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { getList } from "@/api/artist.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      categoryList: []
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {
    this.categoryList = getList();
  },

  methods: {
    queryArtist(cat) {
      this.$router.push({
        path: "/artist",
        query: {
          cat: cat
        }
      });
      this.$emit("queryArtist", cat);
    }
  }
};
</script>
<style lang='scss' scoped>
.artist-choose {
  background-color: #fafafa;
  border: 1px solid #ddd;
  overflow: hidden;
  padding: 36px 16px 900px 16px;
  margin-bottom: -800px;
}
.artist-category {
  text-align: left;
  padding: 16px;
  border-bottom: 1px solid #ddd;
  h3 {
    font-size: 16px;
    line-height: 2em;
    font-weight: 800;
  }
  li {
    font-size: 14px;
    cursor: pointer;
    line-height: 2em;
  }
}
</style>