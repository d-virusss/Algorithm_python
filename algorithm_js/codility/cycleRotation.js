// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  let result = [];
  K = K % A.length;
  deleted_el = A.splice(A.length - K, K);
  result = deleted_el.concat(A);
  return result;
}
