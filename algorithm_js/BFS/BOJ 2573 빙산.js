const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const first_line = input[0].split(" ");
const row = parseInt(first_line[0]);
const col = parseInt(first_line[1]);
let map = [];
let d_ice = [];
let visited = [];
let q = [];
let cx = 0;
let cy = 0;
let nx = 0;
let ny = 0;
let sea_count = 0;
let year = 0;
const d_row = [-1, 0, 1, 0]
const d_col = [0, 1, 0, -1]
for (let i = 0; i < row; i++) {
  visited.push([])
  d_ice.push([])
  for (let j = 0; j < col; j++) {
    visited[i].push(0)
    d_ice[i].push(0)
  }
}
for(let i=1; i<=row; i++){
  map.push(input[i].split(' ').map(x => parseInt(x)))
}
function cal_map(){
  for(let i=0; i<row; i++){
    for(let j=0; j<col; j++){
      if(map[i][j] > 0){
        if (map[i][j] - d_ice[i][j] >= 0) map[i][j] -= d_ice[i][j];
        else map[i][j] = 0;
      }
    }
  }
}
function reset_visited(){
  for(let i=0; i<row; i++){
    for(let j=0; j<col; j++){
      visited[i][j] = 0;
      d_ice[i][j] = 0;
    }
  }
}
function after_year(){
  reset_visited()
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (!(map[i][j] === 0) && (visited[i][j] === 0)) {
        q.push([i, j])
        visited[i][j] = 1
        while (q.length) {
          sea_count = 0;
          [cx, cy] = q.shift()
          for (let d = 0; d < 4; d++) {
            nx = cx + d_row[d]
            ny = cy + d_col[d]
            if (nx >= 0 && nx < row && ny >= 0 && ny < col) {
              if (map[nx][ny] === 0) sea_count++;
              else if (visited[nx][ny] === 0) {
                q.push([nx, ny])
                visited[nx][ny] = 1
              }
            }
          }
          d_ice[cx][cy] = sea_count
        }
      }
    }
  }
  cal_map()
}
function check_chunk(){
  let chunk = 0
  reset_visited()
  for(let i=0; i<row; i++){
    for(let j=0; j<col; j++){
      if(!(map[i][j]===0) && (visited[i][j] === 0)){
        q.push([i,j])
        visited[i][j] = 1
        chunk++
        while(q.length){
          [x, y] = q.shift()
          for (let d = 0; d < 4; d++) {
            nx = x + d_row[d]
            ny = y + d_col[d]
            if (nx >= 0 && nx < row && ny >= 0 && ny < col) {
              if (!(map[nx][ny] === 0) && visited[nx][ny] === 0) {
                q.push([nx, ny])
                visited[nx][ny] = 1
              }
            }
          }
        }
      }
    }
  }
  if(chunk > 1) return false;
  else if(chunk === 1) return true;
  else if(chunk === 0) year = 0; return false;
}

while(check_chunk()){
  year++;
  after_year();
}

console.log(year)