const splitArray = function(array, size){
  let temp = [];
  let len = Math.floor(array.length / size);
  for(let i=0; i< len; i++){
    temp.push(array.splice(0, size))
  }
  return temp;
}
export default splitArray;
