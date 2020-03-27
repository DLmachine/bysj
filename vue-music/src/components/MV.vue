<template>
  <div class="recommend-wrap">
    <div class="recommend">
    <h2 class="title">M V</h2>
    <el-carousel v-bind:autoplay="false" arrow="always"  height="450px">
      <el-carousel-item v-for="(page, pindex) in MvList" :key="pindex">
        <ul class="main clearfix">
          <li  v-for="(item, index) in page" :key="index" class="song-menu-item">
            <div class="show-img scale-img">
              <router-link target="_blank" v-bind:to="'/play/mv/'+item.id">
                <img v-bind:src="item.picUrl" alt="">
                <div class="mask">
                  <i class="el-icon-caret-right"></i>
                </div>
              </router-link>
            </div>
            <h3 class="nowrap-text"><router-link target="_blank" v-bind:to="'/play/mv/'+item.id">{{ item.name }}</router-link></h3>
            <div><span>播放量：{{ Math.floor(item.playCount)}}</span></div>
          </li>
        </ul>
      </el-carousel-item>
    </el-carousel>
  </div>
  </div>
</template>

<script>
export default {
  name: "MV",
  props:[
    "MvList"
  ]
};
</script>

<style scoped>
.recommend-wrap {
  background: #ffffff;
  padding: 20px;
}
.recommend {
}
.song-menu{
  height: auto;;
}
h3{
  margin: 5px 0;
}
.title {
  font-size: 32px;
  text-align: center;
}
.song-menu-item {
  width: 20%;
  float: left;
  padding: 0 20px;
  overflow: hidden;
  margin-bottom: 30px;
}
.show-img{
  position: relative;
  width: 230px;
  height: 130px;
  overflow: hidden;
  transition: all .3s;
}
.show-img:hover .mask{
  opacity: 1;
}

.mask{
  opacity: 0;
  transition: all .3s;
  position: absolute;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.6);
  top: 0;
  left: 0;
  color: #ffffff;
  font-size: 60px;
  padding-top: 30px;
  padding-left: 75px;

}
</style>
