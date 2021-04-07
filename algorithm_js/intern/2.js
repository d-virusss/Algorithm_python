function solution(today, limit){
  let $tbody = document.querySelector('tbody');
  let wrong_count = 0;
  Array.prototype.forEach.call($tbody.children, (el, index) => {
    let is_red = el.style.length === 0 ? false : true;
    if(el.children[2].textContent === ""){ // 반납 안한 경우
      let diff = Date.parse(today) - Date.parse(el.children[1].textContent);
      diff /= 1000; // cal milisec
      diff /= 86400; // cal days
      if((diff > limit && is_red === false) || (diff <= limit && is_red === true)){
        wrong_count += 1;
      } // 연체했는데 색칠 안되어 있는 경우 or 연체안했는데 색칠 되어 있는 경우
    }else{ // 반납 한 경우
      let diff = Date.parse(el.children[2].textContent) - Date.parse(el.children[1].textContent);
      diff /= 1000; // cal milisec
      diff /= 86400; // cal days
      if((diff > limit && is_red === false) || (diff <= limit && is_red === true)){
        wrong_count += 1;
      }
    }
  })
  return wrong_count;
}

console.log(solution("", 7))