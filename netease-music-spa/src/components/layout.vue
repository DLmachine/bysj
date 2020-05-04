<template>
  <div>
    <a-row>
      <a-col :span="24">
        <a-row>
          <div class="g-topbar">
            <div class="m-top">
              <a-col :span="8">
                <div class="logo animation-class">
                  <h1 @click="goHome">
                    <span>MusicRec</span>
                  </h1>
                </div>
              </a-col>
              <a-col :span="8">
                <div class="m-nav">
                  <ul>
                    <li
                      v-for="(item,index) in topLink"
                      :key="index"
                      :class="checkedTopLink==index ?'isTopChecked' : ''"
                      @click="clickTopLink(index)"
                    >
                      <router-link :to="item.link">
                        <span>{{item.span}}</span>
                      </router-link>
                    </li>
                  </ul>
                </div>
              </a-col>
              <a-col :span="4">
                <div class="m-nav-login">
                  <button v-if="!loginSuccess" class="underline-btn" @click="showLoginForm">登录</button>
                  <div v-else>
                    <button class="underline-btn" @click="logout">登出</button>
                    <button class="underline-btn" @click="goMyMusic">{{nickname}}</button>
                    <img class="avatar" v-lazy="avatarUrl" alt="avatar" />
                  </div>
                </div>
              </a-col>
            </div>
            <div class="m-subnav">
              <div class="m-subnav-list">
                <ul>
                  <li
                    v-for="(item,index) in subLink"
                    :key="index"
                    :class="checkedSubLink==index ?'isSubChecked' : ''"
                    @click="clickSubLink(index)"
                  >
                    <router-link :to="item.link">
                      <em>{{item.span}}</em>
                    </router-link>
                  </li>
                </ul>
              </div>
            </div>
            <login-form v-if="loginShow" @confirmLogin="confirmLogin"></login-form>
            <aplayer class="aplayer"></aplayer>
            <my-playlist></my-playlist>
          </div>
        </a-row>
      </a-col>
    </a-row>
    <transition name="fade-transform" mode="out-in">
      <keep-alive include="search">
        <router-view />
      </keep-alive>
    </transition>
  </div>
</template>

<script>
import "@/style/animationClass.scss";
import LoginForm from "./login.vue";
import Aplayer from "./aplayer.vue";
import MyPlaylist from "./myPlaylist.vue";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "",
  props: [""],
  data() {
    return {
      topLink: [
        {
          span: "发现音乐",
          link: "/home"
        },
        {
          span: "我的音乐",
          link: "/my/daily-recommend"
        },
        {
          span: "搜索",
          link: "/search-detail"
        }
      ],
      subLink: [
        {
          span: "推荐",
          link: "/"
        },
        // {
        //   span: "排行榜",
        //   link: "/ranking-list"
        // },
        {
          span: "歌单",
          link: "/playlist"
        },
        // {
        //   span: "主播电台",
        //   link: "/dj-radios"
        // },
        {
          span: "歌手",
          link: "/artist"
        },
        // {
        //   span: "新碟上架",
        //   link: "/new-album"
        // }
      ],
      loginShow: false,
      checkedTopLink: 0,
      checkedSubLink: 0
    };
  },

  components: {
    LoginForm,
    Aplayer,
    MyPlaylist
  },

  computed: {
    ...mapGetters({
      uid: "uid",
      nickname: "nickname",
      avatarUrl: "avatarUrl",
      loginSuccess: "loginSuccess"
    })
  },

  watch: {},

  beforeMount() {},

  mounted() {
    window.sessionStorage.setItem("checkedTopLink", 0);
    window.sessionStorage.setItem("checkedSubLink", 0);
  },
  methods: {
    ...mapActions(["LOGOUT"]),
    clickTopLink(idx) {
      if (idx === 0) {
        window.sessionStorage.setItem("checkedTopLink", idx);
        window.sessionStorage.setItem("checkedSubLink", 0);
        this.checkedTopLink = window.sessionStorage.getItem("checkedTopLink");
        this.checkedSubLink = window.sessionStorage.getItem("checkedSubLink");
      } else if (idx === 1) {
        if (this.$store.getters.loginSuccess) {
          window.sessionStorage.setItem("checkedTopLink", idx);
          window.sessionStorage.setItem("checkedSubLink", -1);
          this.checkedTopLink = window.sessionStorage.getItem("checkedTopLink");
          this.checkedSubLink = window.sessionStorage.getItem("checkedSubLink");
        }
      } else if (idx === 2) {
        window.sessionStorage.setItem("checkedTopLink", idx);
        window.sessionStorage.setItem("checkedSubLink", -1);
        this.checkedTopLink = window.sessionStorage.getItem("checkedTopLink");
        this.checkedSubLink = window.sessionStorage.getItem("checkedSubLink");
      }
    },
    clickSubLink(idx) {
      window.sessionStorage.setItem("checkedTopLink", 0);
      this.checkedTopLink = window.sessionStorage.getItem("checkedTopLink");
      window.sessionStorage.setItem("checkedSubLink", idx);
      this.checkedSubLink = window.sessionStorage.getItem("checkedSubLink");
    },
    showLoginForm() {
      this.loginShow = true;
    },
    confirmLogin() {
      this.loginShow = false;
    },
    async logout() {
      await this.LOGOUT()
        .then(result => {
          this.$message.success("已退出登录");
          this.goHome();
        })
        .catch(err => {});
    },
    goHome() {
      window.sessionStorage.setItem("checkedTopLink", 0);
      window.sessionStorage.setItem("checkedSubLink", 0);
      this.checkedTopLink = window.sessionStorage.getItem("checkedTopLink");
      this.checkedSubLink = window.sessionStorage.getItem("checkedSubLink");
      this.$router.push({
        path: "/"
      });
    },
    goMyMusic() {
      window.sessionStorage.setItem("checkedTopLink", 1);
      window.sessionStorage.setItem("checkedSubLink", -1);
      this.checkedTopLink = window.sessionStorage.getItem("checkedTopLink");
      this.checkedSubLink = window.sessionStorage.getItem("checkedSubLink");
      this.$router.push({
        path: "/my/daily-recommend"
      });
    }
  }
};
</script>
<style lang='scss' scoped>
.g-topbar {
  position: relative;
  z-index: 99;
  width: 100%;
  background-color: #242424;
  color: #333;
}
.m-top {
  position: relative;
  z-index: 1000;
  height: 70px;
  min-width: 1000px;
  box-sizing: border-box;
  color: #ccc;
  background: #242424;
  border-bottom: 1px solid #000;
  .logo {
    height: 70px;
    .icon-netease {
      margin: 0 4px;
    }
    a {
      font-weight: 100;
      font-size: 24px;
      line-height: 70px;
      color: #fff;
      text-decoration: none;
      padding: 0 19px;
    }
  }
  .m-nav {
    text-align: left;
  }
  .m-nav li,
  li span,
  a,
  a em {
    display: inline-block;
    color: #ccc;
    height: 70px;
    font-size: 14px;
    line-height: 70px;
  }
  .m-nav span {
    padding: 0 19px;
  }
  .m-nav-login {
    position: relative;
    .avatar {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      margin: 20px 2px;
      float: right;
    }
    .underline-btn {
      float: right;
      font-size: 14px;
      margin: 0 2px;
      height: 70px;
      line-height: 70px;
      color: #ccc;
      background-color: rgba($color: #000000, $alpha: 0);
      outline: none;
      border: none;
      text-decoration: underline;
      cursor: pointer;
    }
  }

  .isTopChecked {
    background-color: #000;
    & a span {
      color: #fff;
    }
  }
}
.m-subnav {
  background-color: #c20c0c;
  position: relative;
  min-width: 800px;
  height: 34px;
  & .m-subnav-list {
    display: flex;
    flex-wrap: nowrap;
    justify-content: center;
    margin-left: -4%;
  }
  li {
    display: inline-block;
    margin: 4px;
    text-align: center;
    width: 84px;
    height: 24px;
    outline: none;
    cursor: pointer;
    line-height: 24px;
    em {
      display: inline-block;
      width: 100%;
      color: #fff;
    }
  }
  .isSubChecked {
    background-color: #9b0909;
    border-radius: 20px;
  }
}
.aplayer {
  position: fixed;
  left: 0;
  right: 0;
  bottom: -6px;
}
</style>
