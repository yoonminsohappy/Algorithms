function isAdditiveNumber(str){
    //문자열의 길이 < 3
    if(str.length < 3){
      return false;  
    }
    // 문자열 길이 >= 3
    let splitted = str.split('')
    var numArr = [];
    // 문자열을 -> 숫자로 바꾼 배열
    for(var i=0; i<splitted.length; i++){
      splitted[i] = Number(splitted[i]) 
      numArr[i] = splitted[i]
  }
    // 숫자 배열에 대해 조건 판별
  
    for(var i=2; i<numArr.length; i++){
      let sum = numArr[i-1] + numArr[i-2];
      if( sum >= 10 && numArr.length >= 4 ){
        let twoDigit = str.slice(2)
        twoDigit = Number(twoDigit);
        if( sum === twoDigit ){
          return true;
        }
      }
      if( numArr[i-1] + numArr[i-2] !== numArr[i] ){
        return false;
      }  
    }
       return true;
  }
  
  isAdditiveNumber("1"); // false
  isAdditiveNumber("11"); // false
  isAdditiveNumber("112"); // true
  isAdditiveNumber("101"); // true
  isAdditiveNumber("1123"); // true
  isAdditiveNumber("1124"); // false
  isAdditiveNumber("1011"); // true
  isAdditiveNumber("9918"); // true*
  isAdditiveNumber("9917"); // false