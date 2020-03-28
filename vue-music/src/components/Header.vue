<template>
  <div class="header">
    <div class="main clearfix">
      <div class="logo"><img src="../assets/images/logo.png" alt=""></div>
        <ul class="header-nav clearfix">
          <li v-for="(item, index) in navigations" :key="index" @click="active(index)">
              <router-link v-bind:class="activeIndex===index?'nav-link-active':''" v-bind:to="item.path">{{ item.name }}</router-link>
          </li>
        </ul>
        <div class="search-container"><el-input v-model="searchVaue" placeholder="搜索音乐、歌手" suffix-icon="el-icon-search" @keyup.enter.native="submit"></el-input></div>
        <div class="login">
          <span v-if="this.$cookies.get('username')">
            <div class="userbtn">{{this.$cookies.get('username')}} <span  @click="changeUser" class="layouticon"> | <router-link v-bind:to="'/login'"> 注销</router-link></span></div>
          </span>
          <span v-else>
           <router-link v-bind:to="'/login'"> 登录 | 注册</router-link>
          </span>


        </div>
    </div>

  </div>
</template>

<script>
import Login from '../components/Login'

export default {
  name: "HelloWorld",
  components:{
    Login
  },
  created(){
    let match = this.navigations.filter(item=>window.location.pathname.search(item.path) === 0);
    if(match.length){
      this.activeIndex = match[match.length-1].key;
    }
  },
  data() {
    return {
      navigations: [
        {
          key: 0,
          name: "首页",
          path: "/"
        },
        {
          key: 1,
          name: "歌手",
          path: "/artists"
        },
        {
          key: 2,
          name: "专辑",
          path: "/album"
        },
        {
          key: 3,
          name: "排行榜",
          path: "/rank"
        },

        {
          key: 4,
          name: "电台",
          path: "/radio"
        },
        {
          key: 5,
          name: "MV",
          path: "/mv"
        }
      ],
      activeIndex: 0,
      searchVaue: '',
      user:''
    };
  },

  methods: {

    changeUser() {
      this.$cookies.remove('username');
      this.$router.push('/login');
      this.$router.push('/');
    },
    active(index) {
      this.activeIndex = index;
    },
    submit(){
      this.$router.push(`/search?key=${this.searchVaue}`)
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  height: 90px;
  line-height: 90px;
  border-bottom: 1px solid #cccccc;
}
.logo {
  float: left;
  width: 170px;
  margin-right: 22px;
  height: 90px;
}
.logo img {
  width: 100%;
  vertical-align: middle;
}
.header-nav{
  float: left;
  margin-left: 50px;
}
.header-nav li {
  float: left;
  margin-right: 5px;
}
.nav-link-active {
  background-color: #31c27c;
  color: #fff !important;
}
.header-nav li a {
  display: block;
  padding: 0 30px;
  line-height: 90px;
  height: 90px;
  text-align: center;
  font-size: 18px;
  transition: all .5s;
}
.header-nav li a:hover {
  color: #31c27c;
}
.search-container{
  float: left;
  width: 220px;
}
.login{
  position: absolute;
  margin-left: 1300px;
  font-size: 18px;
  width: 220px;
}
.father-ul li:hover .drop-div {
  display: block;
}
.drop-div {
  display: none;
}
</style>
