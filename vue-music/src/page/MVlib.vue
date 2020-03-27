<template>
  <div>
    <Header />
    <MVComponent />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import MVComponent from '../components/MVComponent'
import Footer from '../components/Footer'


export default {
  name: 'Artists',
  components: {
    Header,
    Footer,
    MVComponent
  },
  data(){
    return {
    }
  },


}
</script>

<style>

</style>
