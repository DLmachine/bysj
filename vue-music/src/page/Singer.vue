<template>
  <div>
    <Header />
      <SingerComponent :singerId="singerId" />
      <div class=" main">
        <MV :MvList="MvList"/>
      </div>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import SingerComponent from '../components/SingerComponent'
import MV from '../components/MV'

export default {
  name: 'Artists',
  components: {
    Header,
    Footer,
    SingerComponent,
    MV
  },
  created(){
    const singerId = window.location.pathname.split('/singer/')[1];
    this.singerId =singerId;
    this.getSingerMV(singerId);
  },
  data(){
    return {
      data: null,
      singerId:0,
      MvList:[],
    }
  },
  methods:{
    async getSingerMV(id){
      let result = await this.$hotApi.getSingerMV(id);
      if (result.code === 200) {
        this.MvList = result.data;
      }
    },
  }


}
</script>

<style scoped>

</style>
