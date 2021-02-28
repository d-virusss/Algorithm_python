// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let answer = [];
  answer.push(A[0], -A[0]);
  for(let i=1; i<A.length; i++){
    answer.push(Math.min(Math.abs(answer[i-1]+A[i]), Math.abs(answer[i-1]-A[i])))
  }
  return answer[A.length-1]
}
