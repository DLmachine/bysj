<template>
  <div>
    <a-row class="play-list">
      <a-col :span="14" :offset="5">
        <a-dropdown v-if="!loading" class="categories">
          <a class="ant-dropdown-link" href="#">
            全部分类
            <a-icon type="down" />
          </a>
          <a-menu slot="overlay">
            <a-sub-menu v-for="(cate,index) in categories" :key="index" :title="cate.name">
              <a-menu-item
                v-for="(sub,idx) in cate.list"
                :key="idx"
                @click="getList({cat:sub.name},'cat')"
              >{{sub.name}}</a-menu-item>
            </a-sub-menu>
          </a-menu>
        </a-dropdown>

        <a-skeleton active :loading="loading">
          <a-row type="flex" justify="space-around">
            <a-col
              :span="5"
              class="play-list-item"
              v-for="(item,index) in playlists"
              :key="index"
              @click="goPlaylistDetail(item.id)"
            >
              <div class="img-box">
                <img v-lazy="item.coverImgUrl" width="100%" alt="img" />
              </div>
              <p class="play-list-title">{{item.name}}</p>
            </a-col>
          </a-row>
        </a-skeleton>

        <a-pagination
          @change="onChangePage"
          :current="currentPage"
          :total="100"
          style="margin-top:10px"
        />
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getPlayList, getPlayListCatlist } from "@/api/playList.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      playlists: [],
      categories: [
        {
          name: "语种",
          list: []
        },
        {
          name: "风格",
          list: []
        },
        {
          name: "场景",
          list: []
        },
        {
          name: "情感",
          list: []
        },
        {
          name: "主题",
          list: []
        }
      ],
      cat: "全部",
      currentPage: 1,
      loading: true
    };
  },

  components: {},

  computed: {},

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getList({ cat: "全部", offset: 0 });
    let categories = await getPlayListCatlist();
    console.log(categories);
    for (const item of categories.sub) {
      this.categories[item.category].list.push(item);
    }
    this.loading = false;
  },

  methods: {
    async getList(data, cat) {
      if (cat === "cat") {
        this.currentPage = 1;
        this.cat = data.cat;
      }
      let playlists = await getPlayList({
        cat: data.cat,
        offset: (this.currentPage - 1) * 20
      });
      this.playlists = playlists.playlists.map(item => {
        return {
          coverImgUrl: item.coverImgUrl,
          name: item.name,
          id: item.id
        };
      });
    },
    async onChangePage(cur) {
      this.currentPage = cur;
      await this.getList(
        { cat: this.cat, offset: (this.currentPage - 1) * 20 },
        "page"
      );
    },
    goPlaylistDetail(id) {
      this.$router.push({
        path: "/playlist-detail",
        query: {
          id: id
        }
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.categories {
  margin-left: -88%;
  font-size: 18px;
  color: #333333 !important;
}
.play-list {
  font-size: 16px;
  margin-top: 16px;
  padding-bottom: 100px;
  .play-list-item {
    margin-top: 16px;
    img {
      cursor: pointer;
    }
  }
  .play-list-title {
    font-size: 14px;
    cursor: pointer;
    line-height: 1.5em;
  }
}
.img-box {
  width: 100%;
  position: relative;
  height: 0;
  padding-bottom: 100%;
  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
  }
}
</style>
