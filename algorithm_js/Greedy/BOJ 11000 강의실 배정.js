const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split("\n");
const N = parseInt(input[0]);
let classes = [];
for(let i=0; i<N; i++){
  classes.push(input[i+1].split(" ").map(el => parseInt(el)));
}

let checked = [];
for(let i=0; i<N; i++){
  checked.push(0);
}
let count = 0;
let end_time = -1;
classes.sort(function (a, b) {
  if (a[0] === b[0]) {
    return a[1] - b[1];
  }
  return a[0] - b[0];
})
console.log(classes);
function reset_checked(){
  for(let i=0; i<checked.length; i++){
    checked[i] = 0;
  }
}
function do_class(){
  for(let i=classes.length-1; i>=0; i--){
    if(checked[i] === 1){
      classes.splice(i, 1)
    }
  }
}

while(classes.length){
  count++;
  end_time = classes[0][1];
  checked[0] = 1;
  for(let i=1; i<classes.length; i++){
    if(classes[i][0] >= end_time){
      end_time = classes[i][1];
      checked[i] = 1;
    }
  }
  do_class();
  reset_checked();
}

console.log(count)