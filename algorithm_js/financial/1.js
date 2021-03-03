// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(riddle) {
  // write your code in JavaScript (Node.js 8.9.4)
  let alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'];
  
  let result = "";
  let str_len = riddle.length;
  for(let i=0; i<str_len; i++){
    if(riddle[i] !== '?') result += riddle[i];
    else{
      if(str_len === 1){ // 주어진 riddle이 한 글자일 경우
        result += alpha[0];
      }
      else if(i === 0){ // 첫 letter인 경우
        if(riddle[i+1] === '?') result += alpha[0]; // 첫 letter 다음 글자가 '?'라면
        else{
          for(let j=0; j<26; j++){
            if(riddle[i+1] !== alpha[j]){
              result += alpha[j];
              break;
            }
          }
        }
      }
      else if(i === (str_len-1)){ // 마지막 letter인 경우
        for(let j=0; j<26; j++){
          if(result[i-1] !== alpha[j]){
            result += alpha[j];
            break;
          }
        }
      }
      else{ // 중간일 경우
        if(riddle[i+1] === '?'){
          for(let j=0; j<26; j++){
            if(result[i-1] !== alpha[j]){
              result += alpha[j];
              break;
            } 
          }
        }
        else{
          for(let j=0; j<26; j++){
            if((result[i-1] !== alpha[j]) && (riddle[i+1] !== alpha[j])){
              result += alpha[j];
              break;
            }
          }
        }
      }
    }
  }
  return result;
}

let riddle = "?????????";
console.log(solution(riddle));