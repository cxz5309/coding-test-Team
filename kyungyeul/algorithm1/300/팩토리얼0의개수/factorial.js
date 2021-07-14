const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let n = Number(input[0]);
  let count = 0;
  while (n >= 5) {
    count += parseInt(n / 5);
    parseInt((n /= 5));
  }
  console.log(count);
});
