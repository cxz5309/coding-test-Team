const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  for (let i = 0; i < input.length; i++) {
    let str = input[i].split("");
    let result = [0, 0, 0, 0];

    str.map((value) => {
      if (value.match(/^[a-z]/g)) {
        result[0] += 1;
      } else if (value.match(/^[A-Z]/g)) {
        result[1] += 1;
      } else if (value.match(/^[0-9]/g)) {
        result[2] += 1;
      } else {
        result[3] += 1;
      }
    });
    console.log(result.join(" "));
  }
});
