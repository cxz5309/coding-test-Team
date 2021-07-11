const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let word = input[0].split("");
  let arr = [];
  const ROT = (x) => {
    x.map((value) => {
      if (value.match(/^[A-Z]/g)) {
        if (value.charCodeAt(0) <= 77) {
          let a = value.charCodeAt(0) + 13;
          arr.push(String.fromCharCode(a));
        } else {
          let a = value.charCodeAt(0) - 13;
          arr.push(String.fromCharCode(a));
        }
      } else if (value.match(/^[a-z]/g)) {
        if (value.charCodeAt(0) <= 109) {
          let a = value.charCodeAt(0) + 13;
          arr.push(String.fromCharCode(a));
        } else {
          let a = value.charCodeAt(0) - 13;
          arr.push(String.fromCharCode(a));
        }
      } else if (value.match(/^[0-9]/g)) {
        arr.push(value);
      } else {
        arr.push(value);
      }
    });
  };
  ROT(word);
  console.log(arr.join(""));
});
