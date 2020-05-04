<template>
  <div>
    <a-row>
      <a-col :span="14" :offset="5">
        <a-row>
          <a-col :span="4">
            <choose-category @queryArtist="queryArtist"></choose-category>
          </a-col>
          <a-col :span="20">
            <recommend-artist v-if="!isQuery"></recommend-artist>
            <query-artist-by-cat v-else :artistList="artistList"></query-artist-by-cat>
          </a-col>
        </a-row>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import ChooseCategory from "./components/chooseCategory";
import RecommendArtist from "./components/recommendArtist";
import QueryArtistByCat from "./components/queryArtistByCat";
import { getArtistList } from "@/api/artist";
export default {
  name: "",
  props: [""],
  data() {
    return {
      isQuery: false,
      artistList: []
    };
  },

  components: {
    ChooseCategory,
    RecommendArtist,
    QueryArtistByCat
  },

  computed: {},

  watch: {},

  beforeMount() {},

  mounted() {},

  methods: {
    async queryArtist(cat) {
      if(cat != 9999){
        this.isQuery = true;
        await this.getArtists();
      } else {
        this.isQuery = false;
      }
    },
    async getArtists() {
      let res = await getArtistList({
        cat: this.$route.query.cat,
        limit: 40,
        offset: (this.currentPage - 1) * 20
      });
      this.artistList = res.artists.map(item => {
        return {
          id: item.id,
          picUrl: item.picUrl,
          name: item.name
        };
      });
    },
  }
};
</script>
<style lang='scss' scoped>
</style>
