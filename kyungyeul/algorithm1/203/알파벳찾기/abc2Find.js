const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let a = input[0];
  let result = [];
  for (let i = 97; i <= 122; i++) {
    result.push(a.indexOf(String.fromCharCode(i)));
  }
  console.log(result.join(" "));
  process.exit();
});
