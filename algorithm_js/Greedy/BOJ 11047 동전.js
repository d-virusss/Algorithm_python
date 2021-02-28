const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const first_line = input[0].split(" ");
const N = parseInt(first_line[0]);
const goal = parseInt(first_line[1]);
const coins =[];
for(let i=0; i<N; i++){
  coins.push(parseInt(input[i+1]));
}
let remain = goal;
let count = 0;
for(let i=coins.length-1; i>=0; i--){
  if(remain === 0) break;
  while(remain >= coins[i]){
    remain -= coins[i];
    count++;
  }
}
console.log(count);