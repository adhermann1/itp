let size = 4;
let chess = "";
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    if ((i + j) % 2 == 0)
      chess += " ";
    else
      chess += "#";
  }
  chess += "\n";
}
console.log(chess);
