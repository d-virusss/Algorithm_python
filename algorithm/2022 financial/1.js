function solution(maps, p, r) {
  let killed = 0;

  const applyMagic = (sx, sy) => {
    let current_kill = 0;
    // for(let x = 0; x < maps.length; x++) {
    //   for(let y = 0; y < maps.length; y++) {
    //     if(){ // 마법범위에 포함되는지 check
    //       if(){ // 외곽인경우
    //         if(map[x][y] <= p/2) current_kill += 1;
    //       }
    //       else { // 외곽아닐경우
    //         if(map[x][y] <= p) current_kill += 1;
    //       }
    //     }
    //   }
    // }

    for (let i = 1; i <= r/2; i++) {
      let first = sx-row*2;
      for(let j = 1; j<=i*2; j++){
        let row = sx-
      }
    }
    if (current_kill > killed) killed = current_kill;
  };

  for (let x = 1; x <= maps.length + 1; x++) {
    for (let y = 1; y <= maps.length + 1; y++) {
      applyMagic(x, y);
    }
  }

  return killed;
}
