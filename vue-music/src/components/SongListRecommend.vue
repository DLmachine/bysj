<template>
  <div class="recommend-wrap">
    <div class="recommend">
    <h2 class="title">歌单推荐</h2>
    <el-carousel v-bind:autoplay="false" arrow="always"  height="350px">
      <el-carousel-item v-for="(page, pindex) in songlist" :key="pindex">
        <ul class="main clearfix">
          <li  v-for="(item, index) in page" :key="index" class="song-menu-item">
            <div class="show-img scale-img">
              <router-link target="_blank" v-bind:to="'/play/songlist/'+item.id">
                <img v-bind:src="item.picUrl" alt="">
                <div class="mask">
                  <i class="el-icon-caret-right"></i>
                </div>
              </router-link>
            </div>
            <h3 class="nowrap-text"><router-link target="_blank" v-bind:to="'/play/songlist/'+item.id">{{ item.name }}</router-link></h3>
            <p>播放量：{{ Math.floor(item.playCount)}}</p>
          </li>
        </ul>
      </el-carousel-item>
    </el-carousel>
  </div>
  </div>
</template>

<script>
export default {
  name: "SongListRecommend",
  props: ["songlist"]
};
</script>

<style scoped>
.recommend-wrap {
  background: #f5f5f5;
  height: 530px;
  padding: 20px;
}
.recommend {
}
.song-menu{
  height: auto;;
}
.title {
  font-size: 32px;
  text-align: center;
}
.song-menu-item {
  width: 20%;
  float: left;
  padding-right: 15px;
}
.show-img{
  position: relative;
  width: 230px;
  height: 230px;
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
  padding-top: 70px;
  padding-left: 75px;

}
</style>
