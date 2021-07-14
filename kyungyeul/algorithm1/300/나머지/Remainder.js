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
  const c = n[2];
  const one = (a + b) % c;
  const two = ((a % c) + (b % c)) % c;
  const three = (a * b) % c;
  const four = ((a % c) * (b % c)) % c;
  console.log(one);
  console.log(two);
  console.log(three);
  console.log(four);
});
