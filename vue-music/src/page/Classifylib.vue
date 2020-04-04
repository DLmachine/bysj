<template>
  <div>
    <Header />
    <ClassifyComponent />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import ClassifyComponent from '../components/ClassifyComponent'
import Footer from '../components/Footer'


export default {
  name: 'Classify',
  components: {
    Header,
    Footer,
    ClassifyComponent
  },
  data(){
    return {
    }
  },


}
</script>

<style>

</style>
