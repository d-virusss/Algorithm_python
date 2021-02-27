// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
  // write your code in JavaScript (Node.js 8.9.4)
  let binary = N.toString(2);
  let binary_arr = binary.split("");
  let one_count = binary_arr.filter((num) => {
    return num === "1";
  });
  if (!binary.includes("0") || one_count.length === 1) {
    return 0;
  }
  let max = -1
  let count = 0
  for (let i = 0; i < binary_arr.length; i++) {
    if (binary_arr[i] === "1") {
      if (count > max) max = count;
      count = 0;
    }
    else {
      count++;
    }
  }
  return max;
}
let num = 1100
let answer = solution(num)
console.log(num.toString(2))
console.log(answer)