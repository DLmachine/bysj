<template>
  <div>
    <Header />
    <ArtistsComponent/>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import ArtistsComponent from '../components/ArtistsComponent'

export default {
  name: 'Artists',
  components: {
    Header,
    ArtistsComponent,
    Footer
  },
  data(){
    return {
    }
  },


}
</script>

<style>

</style>
