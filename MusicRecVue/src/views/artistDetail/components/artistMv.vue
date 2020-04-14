<<<<<<< HEAD
<template>
  <div>
    <a-skeleton active :loading="loading">
      <div class="album-list">
        <a-row type="flex" justify="start">
          <a-col
            :span="5"
            style="margin:16px"
            class="album-list-item"
            v-for="(item,index) in mvList"
            :key="index"
            @click="goMvDetail(item.id)"
          >
            <img v-lazy="item.imgurl16v9" width="100%" alt="img" style="cursor:pointer"/>
            <p class="album-list-title">{{item.name}}</p>
          </a-col>
        </a-row>
      </div>
    </a-skeleton>
  </div>
</template>

<script>
import { getArtistMv } from "@/api/artist.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      mvList: [],
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getMv();
    this.loading = false;
  },

  methods: {
    async getMv() {
      let res = await getArtistMv(this.$route.query.id);
      this.mvList = res.mvs;
    },
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