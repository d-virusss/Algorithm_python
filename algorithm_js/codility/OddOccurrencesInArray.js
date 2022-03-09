function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let countObj = {};
  A.forEach((el) => {
    if (countObj[el] === undefined) {
      countObj[el] = 1;
    } else {
      countObj[el] += 1;
    }
  });
  let result;
  Object.entries(countObj).find(([key, value]) => {
    if (value % 2 === 1) result = key;
  });
  return result;
}

let nums = [9, 3, 9, 3, 9, 7, 9];
console.log(solution(nums));

// 7:47 pm 시작
// 8:13 pm 제출
// Correctness 100% / Performance 75%
// n = 999,999 일 때, TIMEOUT ERROR, running time: 1.640 sec., time limit: 1.472 sec.
