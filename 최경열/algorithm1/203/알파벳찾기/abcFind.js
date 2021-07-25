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
  const arr = new Array(26).fill(-1);
  for (let i in arr) {
    for (let j in word) {
      let x = word[j];
      arr[x.charCodeAt(0) - 97] = word.indexOf(x);
      //Arroy.indexOf()은 찾는 첫번째 인덱스를 반환,없으면-1을한다
    }
  }
  console.log(arr.join(" "));
});
