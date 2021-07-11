const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const word = input[0];
  const arr = new Array(26).fill(0);
  for (let i in word) {
    let j = word[i];
    arr[j.charCodeAt(0) - 97] += 1;
  }
  console.log(arr.join(" "));
});
