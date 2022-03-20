function solution(s1, s2) {
  var result = 0;
  let nextPos = {
    0: [1, 5, 6],
    1: [0, 6, 2],
    2: [1, 6, 3],
    3: [2, 6, 4],
    4: [3, 5, 6],
    5: [0, 6, 4],
    6: [0, 1, 2, 3, 4, 5],
  };
  let visited = {};

  let q = [[s1, s1.indexOf(0), result]];

  while (q.length) {
    let nextInfo = q.shift();
    let [nextS1, zero, count] = nextInfo;

    visited[String(nextS1)] = true;

    // console.log(nextS1);
    // console.log(s2);

    if (nextS1.toString() === s2.toString()) {
      result = count;
      break;
    }

    for (let i of nextPos[zero]) {
      console.log(i);
      let tmpS1 = nextS1.slice();
      let tmp = tmpS1[i];
      tmpS1[i] = tmpS1[zero];
      tmpS1[zero] = tmp;

      console.log(String(tmpS1));

      if (visited[String(tmpS1)] !== undefined) continue;
      q.push([tmpS1, i, count + 1]);
    }
  }

  console.log("result == ");
  console.log(result);
  return result;
}

let s1 = [1, 2, 3, 0, 6, 5, 4];
let s2 = [1, 2, 3, 4, 5, 6, 0];

solution(s1, s2);
