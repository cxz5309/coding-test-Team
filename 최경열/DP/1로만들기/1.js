const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const x = Number(input[0]);
  d = [];
  d[1] = 0;
  for (var i = 2; i <= x; i++) {
    d[i] = d[i - 1] + 1;
    if (i % 2 == 0) {
      d[i] = Math.min(d[i], d[i / 2] + 1);
    }
    if (i % 3 == 0) {
      d[i] = Math.min(d[i], d[i / 3] + 1);
    }
  }
  console.log(d[x]);
});
