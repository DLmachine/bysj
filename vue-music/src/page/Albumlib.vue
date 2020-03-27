<template>
  <div>
    <Header />
    <AlbumComponent/>
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import AlbumComponent from '../components/AlbumComponent'

export default {
  name: 'Album',
  components: {
    Header,
    AlbumComponent,
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
