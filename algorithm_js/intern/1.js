function solution(A){
  let first_case = [1, 0];
  let second_case = [0, 1];
  let first_count = 0;
  let second_count = 0;
  for(let i = 0; i<A.length; i++){
    if(A[i] != first_case[(i%2)]) first_count += 1;
    if(A[i] != second_case[(i%2)]) second_count += 1;
  }
  let result = first_count > second_count ? second_count : first_count;
  console.log(first_count);
  console.log(second_count);
  return result;
}

let arr = [0,1,1,0];
let answer = solution(arr);
console.log(answer);