const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let word = input[0];
  let arr = [];
  const x = (value) => {
    for (let i = 0; i < word.length; i++) {
      arr.push(word.slice(i, word.length));
    }
    arr.sort();
    console.log(arr.join(" "));
  };
  x(word);
});
