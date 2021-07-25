const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const a = Number(input[0]);
  const b = input[1].split(" ").map(Number);
  let result = 0;
  for (i in b) {
    let count = 0;
    if (b[i] > 1) {
      for (let j = 2; j < b[i] + 1; j++) {
        if (b[i] % j == 0) {
          count += 1;
        }
      }
      if (count == 1) {
        result += 1;
      }
    }
  }
  console.log(result);
});
