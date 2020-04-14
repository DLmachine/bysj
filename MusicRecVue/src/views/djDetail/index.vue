<template>
  <div class="playlist-detail-container">
    <a-row>
      <a-col :span="14" :offset="5">
        <a-skeleton active :loading="loading">
          <div class="playlist-detail">
            <a-row>
              <a-col :span="5">
                <img v-lazy="djRadio.picUrl" width="100%" style="margin-top:24px" alt="电台" />
              </a-col>
              <a-col :span="18" :offset="1">
                <svg class="icon" aria-hidden="true" style="font-size:100px; margin-right:16px;">
                  <use xlink:href="#icon-zhubodiantaidaiditu" />
                </svg>
                <h1>{{djRadio.name}}</h1>
                <div class="playlist-creator">
                  <img v-lazy="djRadio.dj.avatarUrl" width="36px" alt />
                  <span>{{djRadio.dj.nickname}}&nbsp;&nbsp;于&nbsp;&nbsp;{{djRadio.createTime}}&nbsp;&nbsp;创建</span>
                  <a-button @click.once="addMusicList" style="margin-left: 20px">
                    <svg
                      class="icon"
                      aria-hidden="true"
                      style="font-size:16px; margin-right:16px;"
                    >
                      <use xlink:href="#icon-play1" />
                    </svg>加入播放列表
                  </a-button>
                </div>
                <div class="tag">
                  <span>最近更新：{{djRadio.lastProgramCreateTime}}</span>
                </div>
                <div class="tag">
                  <span>标签：</span>
                  <a-tag color="pink">{{djRadio.category}}</a-tag>
                </div>
                <div>
                  介绍：
                  <p>{{djRadio.description}}</p>
                </div>
              </a-col>
            </a-row>
          </div>
        </a-skeleton>

        <a-skeleton active :loading="loading">
          <div>
            <div class="list-title">
              <span style="font-size:24px">节目列表</span>
              <span>共{{djRadio.programCount}}首</span>
            </div>
            <a-table :dataSource="djRadio.tracks">
              <a-table-column title key="action" width="10%">
                <template slot-scope="text, record">
                  <span>
                    <svg class="icon play-icon" aria-hidden="true" @click.once="addMusic(record)">
                      <use xlink:href="#icon-play1" />
                    </svg>
                  </span>
                </template>
              </a-table-column>
              <a-table-column title="节目标题" width="25%" key="title">
                <template slot-scope="text, record">
                  <a-popover placement="top">
                    <template slot="content">
                      <span>{{record.name}}</span>
                    </template>
                    <span>{{record.name}}</span>
                  </a-popover>
                </template>
              </a-table-column>
              <a-table-column
                title="播放次数"
                width="15%"
                key="listenerCount"
                align="center"
              >
                <template slot-scope="text, record">
                  <a-popover placement="top">
                    <template slot="content">
                      <span>{{record.listenerCount}}</span>
                    </template>
                    <span>{{record.listenerCount}}</span>
                  </a-popover>
                </template>
              </a-table-column>
              <a-table-column title="节目描述" key="description">
                <template slot-scope="text, record">
                  <a-popover placement="top">
                    <template slot="content">
                      <span>{{record.description}}</span>
                    </template>
                    <span>{{record.description}}</span>
                  </a-popover>
                </template>
              </a-table-column>
            </a-table>
          </div>
        </a-skeleton>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getDjDetail, getDjProgram } from "@/api/dj.js";
import { mapActions } from "vuex";
import Bus from "@/utils/bus.js";
import { formatTime } from "@/utils/index";
export default {
  name: "",
  props: [""],
  data() {
    return {
      djRadio: {
        picUrl: "",
        dj: {
          avatarUrl: "",
          nickname: "",
          djId: ""
        },
        description: "",
        name: "",
        id: "",
        category: "",
        subCount: "",
        shareCount: "",
        programCount: "",
        lastProgramCreateTime: "",
        createTime: "",
        tracks: []
      },
      loading: true
    };
  },

  components: {},

  computed: {
    rid() {
      return this.$route.query.rid;
    }
  },

  watch: {
    $route(to, from) {
      this.getDjDetail();
      this.getDjProgram();
    }
  },

  beforeMount() {},

  async mounted() {
    await this.getDjDetail();
    await this.getDjProgram();
    this.loading = false;
  },

  methods: {
    ...mapActions(["SET_CURRENT_MUSIC_ACTION"]),
    async getDjDetail() {
      let res = await getDjDetail(this.rid);
      this.djRadio.picUrl = res.djRadio.picUrl;
      this.djRadio.dj.avatarUrl = res.djRadio.dj.avatarUrl;
      this.djRadio.dj.nickname = res.djRadio.dj.nickname;
      this.djRadio.dj.djId = res.djRadio.id;
      this.djRadio.description = res.djRadio.desc;
      this.djRadio.name = res.djRadio.name;
      this.djRadio.id = res.djRadio.id;
      this.djRadio.category = res.djRadio.category;
      this.djRadio.subCount = res.djRadio.subCount;
      this.djRadio.shareCount = res.djRadio.shareCount;
      this.djRadio.programCount = res.djRadio.programCount;
      this.djRadio.lastProgramCreateTime = formatTime(
        res.djRadio.lastProgramCreateTime,
        "{y}-{m}-{d}"
      );
      this.djRadio.createTime = formatTime(
        res.djRadio.createTime,
        "{y}-{m}-{d}"
      );
    },
    async getDjProgram() {
      let res = await getDjProgram({
        rid: this.rid,
        limit: this.djRadio.programCount
      });
      this.djRadio.tracks = res.programs.map(item => {
        return {
          id: item.mainSong.id,
          name: item.mainSong.name,
          artist: this.djRadio.dj.nickname,
          artistId: this.djRadio.id,
          cover: item.coverUrl,
          description: item.description,
          listenerCount: item.listenerCount,
          key: item.mainSong.id,
          theme: [255, 255, 255],
          songType: "dj"
        };
      });
    },
    addMusicList() {
      Bus.$emit("add", { list: this.djRadio.tracks, type: "program" });
      this.$message.success("已加入播放列表！");
    },
    async addMusic(song) {
      this.SET_CURRENT_MUSIC_ACTION(song)
        .then(result => {
          Bus.$emit("play", result);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
<style lang='scss' scoped>
.playlist-detail-container {
  padding-bottom: 100px;
  font-size: 14px;
  .play-icon {
    margin-left: 40%;
    font-size: 24px;
    cursor: pointer;
  }
  .list-title {
    text-align: left;
    margin-bottom: 10px;
    & > span {
      margin: 10px;
    }
  }
}
.playlist-detail {
  text-align: left;
  margin-top: 16px;
  padding-bottom: 30px;
  h1 {
    font-size: 24px;
    display: inline;
    position: relative;
    top: -26px;
  }
  .playlist-creator {
    font-size: 14px;
    line-height: 3em;
    height: 40px;
    margin: -16px 0 16px 0;
    img {
      margin-right: 16px;
      float: left;
      clear: both;
      border-radius: 50%;
    }
  }
  .tag {
    font-size: 14px;
    margin: 14px 0;
  }
}
</style>