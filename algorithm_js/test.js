let checked = [1, 0, 1, 0, 0];
let classes = [1,3,5,7,9];

for (let i = classes.length - 1; i >= 0; i--) {
  if (checked[i] === 1) {
    classes.splice(i, 1)
  }
}

console.log(classes)