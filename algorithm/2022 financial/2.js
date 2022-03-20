function solution(matches, me, opp) {
  let answer = 0;

  let max = Math.max(...matches);
  let left_child = [];
  let right_child = [];

  for (let i = 0; i <= max; i++) {
    left_child[i] = 0;
    right_child[i] = 0;
  }

  matches.forEach((el, idx) => {
    if (left_child[el] === 0) left_child[el] = idx;
    else right_child[el] = idx;
  });

  while (me !== opp) {
    me = matches[me];
    opp = matches[opp];

    if (left_child[me] !== 0 && right_child[me] !== 0) answer += 1;
  }

  return answer;
}
