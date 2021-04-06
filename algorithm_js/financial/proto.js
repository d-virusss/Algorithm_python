function solution(A){
  function nuar(val){
    this._value = val;
  }
  nuar.prototype.value = function(){
    return this._value;
  }

  let arr = []
  A.forEach(el => {
    arr.push(new nuar(el));
  })

  return arr;
}

let arr = [3,9,11,2,1];
let result = solution(arr);
console.log(result)