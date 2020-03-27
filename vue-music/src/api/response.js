const response = function(code, data, desc=""){
  return {
    code,
    data,
    desc,
  }
}
export default response;
