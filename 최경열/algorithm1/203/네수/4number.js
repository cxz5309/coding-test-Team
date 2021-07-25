const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let a = input[0].split(" ");
  let ab = Number(a[0] + a[1]);
  let cd = Number(a[2] + a[3]);
  console.log(ab + cd);
});
