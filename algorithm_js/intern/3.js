function solution(A){
  let index = -1;
  let crnt_max = A[0];
  let storage = [];
  let slice_count = 1;
  for(let i=1; i<A.length; i++){
    if(A[i] > crnt_max){
      storage.push(crnt_max);
      crnt_max = A[i];
      slice_count += 1;
      index += 1;
    }else if(index >= 0){
      if(A[i] < storage[index]){
        slice_count = 1;
      }
    }
  }
  return slice_count;
}

let arr = [2,1,6,4,3,7];
console.log(solution(arr));