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
  for (let i = 1; i <= a; i++) {
    let data = input[i].split(" ");
    let arr = [];
    for (let j in data) {
      let result = data[j].split("").reverse().join("");
      arr.push(result);
    }
    console.log(arr.join(" "));
  }
  process.exit();
});
