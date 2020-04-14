<template>
  <div class="userPlayList">
    <a-row type="flex" justify="space-around">
      <a-divider orientation="left" style="font-weight:bold"
        >每日推荐</a-divider
      >
      <a-list itemLayout="horizontal" style="width:100%">
        <a-list-item>
          <a-list-item-meta description="根据你的口味生成，每天6:00更新">
            <p slot="title" class="playlist-title" @click="goDailyRecommend">
              每日歌曲推荐
            </p>
            <a-avatar
              slot="avatar"
              :src="avatarUrl"
              class="playlist-cover"
              @click="goDailyRecommend"
            />
          </a-list-item-meta>
        </a-list-item>
        <a-list-item>
          <a-list-item-meta :description="'for - ' + nickname">
            <p slot="title" class="playlist-title" @click="goDailyPlaylist">
              每日歌单推荐
            </p>
            <a-avatar
              slot="avatar"
              :src="avatarUrl"
              class="playlist-cover"
              @click="goDailyPlaylist"
            />
          </a-list-item-meta>
        </a-list-item>
      </a-list>
      <a-divider orientation="left" style="font-weight:bold"
        >创建的歌单</a-divider
      >
      <a-list
        itemLayout="horizontal"
        :dataSource="userPlaylist"
        style="width:100%"
      >
        <a-list-item slot="renderItem" slot-scope="item, index">
          <a-list-item-meta :description="item.trackCount + '首'">
            <p
              slot="title"
              class="playlist-title"
              @click="showPlaylist({ playlist: item, type: 'self' })"
            >
              {{ item.name }}
            </p>
            <a-avatar
              slot="avatar"
              :src="item.coverImgUrl"
              class="playlist-cover"
              @click="showPlaylist({ playlist: item, type: 'self' })"
            />
          </a-list-item-meta>
        </a-list-item>
      </a-list>
      <a-divider orientation="left" style="font-weight:bold"
        >收藏的歌单</a-divider
      >
      <a-list
        itemLayout="horizontal"
        :dataSource="subPlaylist"
        style="width:100%"
      >
        <a-list-item slot="renderItem" slot-scope="item, index">
          <a-list-item-meta :description="item.trackCount + '首'">
            <p
              slot="title"
              class="playlist-title"
              @click="showPlaylist({ playlist: item, type: 'other' })"
            >
              {{ item.name }}
            </p>
            <a-avatar
              slot="avatar"
              :src="item.coverImgUrl"
              class="playlist-cover"
              @click="showPlaylist({ playlist: item, type: 'other' })"
            />
          </a-list-item-meta>
        </a-list-item>
      </a-list>
    </a-row>
  </div>
</template>

<script>
import { getUserPlaylist } from "@/api/user";
import { mapGetters } from "vuex";
import Bus from "@/utils/bus.js";
export default {
  name: "",
  props: [""],
  data() {
    return {
      userPlaylist: [],
      subPlaylist: []
    };
  },

  components: {},

  computed: {
    ...mapGetters(["account", "profile", "uid", "nickname", "avatarUrl"])
  },

  watch: {},

  beforeMount() {},

  async mounted() {
    await this.getUserPlaylist();
    Bus.$on("unsubscribe", data => {
      this.subPlaylist = this.subPlaylist.filter(item => {
        return item.id !== data;
      });
    });
  },

  methods: {
    async getUserPlaylist() {
      let res = await getUserPlaylist(this.uid);
      this.userPlaylist = res.playlist.filter(item => {
        return item.creator.userId == this.uid;
      });
      this.subPlaylist = res.playlist.filter(item => {
        return item.creator.userId != this.uid;
      });
    },
    showPlaylist(playlist) {
      this.$emit("showPlaylist", playlist);
    },
    goDailyRecommend() {
      this.$emit("closePlaylist");
      this.$router.push({
        path: "/my/daily-recommend"
      });
    },
    goDailyPlaylist() {
      this.$emit("closePlaylist");
      this.$router.push({
        path: "/my/daily-playlist"
      });
    }
  }
};
</script>
<style lang="scss" scoped>
.userPlayList {
  padding: 36px 16px 100px 16px;
  text-align: left;
  border: 1px solid rgb(232, 232, 232);
  .playlist-title {
    color: #333;
  }
  .playlist-cover {
    cursor: pointer;
    width: 46px;
    height: 46px;
  }
}
</style>
