<template>
  <div>
    <Header />
    <RankComponent />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import RankComponent from '../components/RankComponent'
import Footer from '../components/Footer'


export default {
  name: 'Artists',
  components: {
    Header,
    Footer,
    RankComponent
  },
  data(){
    return {
    }
  },


}
</script>

<style>

</style>
