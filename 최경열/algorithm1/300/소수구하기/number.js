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
  let x = a[0];
  let y = a[1];

  const isPrime = (num) => {
    let sqrt = parseInt(Math.sqrt(num));
    if (num == 1) {
      return false;
    } else {
      for (let i = 2; i <= sqrt; i++) {
        if (num % i == 0) {
          return false;
        }
      }
      return true;
    }
  };

  for (let i = x; i <= y; i++) {
    if (isPrime(i)) {
      console.log(i);
    }
  }
});
