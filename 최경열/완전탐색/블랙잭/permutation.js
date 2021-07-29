const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const a = input[0].split(" ").map(Number);
  const n = a[0];
  const m = a[1];
  const arr = input[1].split(" ").map(Number);
  let result = 0;
  for (let x = 0; x < arr.length; x++) {
    for (let y = x + 1; y < arr.length; y++) {
      for (let z = y + 1; z < arr.length; z++) {
        if (arr[x] + arr[y] + arr[z] > m) {
          continue;
        } else {
          result = Math.max(result, arr[x] + arr[y] + arr[z]);
        }
      }
    }
  }
  console.log(result);
});
