const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const n = Number(input[0]);
  for (let i = 1; i <= n; i++) {
    let z = input[i].split(" ").map(Number);
    let x = z[0];
    let y = z[1];
    big = Math.max(x, y);
    small = Math.min(x, y);
    while (small != 0) {
      c = big % small;
      big = small;
      small = c;
    }
    console.log((x * y) / big);
  }
});
