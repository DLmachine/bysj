
const state = {
  data: []
}

const mutations = {
  setRankData(state, {id, data}){
    state.data[id]=data;
  },
}


export default {
  state,
  mutations
}
