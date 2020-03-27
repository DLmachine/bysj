<template>
  <div>
    <Header />
    <RadioComponent />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import RadioComponent from '../components/RadioComponent'
import Footer from '../components/Footer'


export default {
  name: 'Artists',
  components: {
    Header,
    Footer,
    RadioComponent
  },
  data(){
    return {
    }
  },


}
</script>

<style>

</style>
