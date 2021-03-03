// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
class el {
  constructor(root, data) {
    this.value = root;
    this.data = data;
  }
  value(){
    return this.data;
  }
}
class f_el extends el{
  constructor(root, data){
    super(root)
    this.data = data;
  }
  value(){
    return this.data;
  }
}

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  const N = A.length;
  let result = {};
  for (let i = 0; i < N; i++) {
    let tmp_el = new el(N, A[i]);
    let result_el = Object.create(tmp_el);
    result_el.value = function(){
      return this.data;
    }
    result[i] = result_el;
  }
  
  return result;
}

const res = solution([1,2,3]);
console.log(res);