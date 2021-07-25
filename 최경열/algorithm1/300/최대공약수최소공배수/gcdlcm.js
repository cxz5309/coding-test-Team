const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const n = input[0].split(" ").map(Number);
  const a = n[0];
  const b = n[1];
  big = Math.max(a, b);
  small = Math.min(a, b);
  while (small != 0) {
    c = big % small;
    big = small;
    small = c;
  }
  console.log(big);
  console.log((a * b) / big);
});
