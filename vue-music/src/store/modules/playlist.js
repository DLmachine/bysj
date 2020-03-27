
const state = {
  data: null
}

const mutations = {
  setPlaylist(state, {data}){
    state.data=data;
  },
}


export default {
  state,
  mutations
}
