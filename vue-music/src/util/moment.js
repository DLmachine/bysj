export default class moment {
  static formatDate(obj){
    var date =  new Date(obj);
    var y = 1900+date.getYear();
    var m = "0"+(date.getMonth()+1);
    var d = "0"+date.getDate();
    return y+"-"+m.substring(m.length-2,m.length)+"-"+d.substring(d.length-2,d.length);
  }

  static getNowFormatDate(){
    var date = new Date();
    var seperator1 = "-";
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = year + seperator1 + month + seperator1 + strDate;
    return currentdate;
  }

  static clock(timeStamp){
    let seconds  = timeStamp / 1000;
    let minutes = Math.floor(seconds / 60)>9?Math.floor(seconds / 60): '0'+Math.floor(seconds / 60);
    return minutes+ ':'+  Math.floor(seconds % 60);
  }
}
