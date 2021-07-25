const stack = [];
let top = 0;
let answer = "";

const result = {
  push: (x) => {
    stack.push(x);
  },
  pop: () => {
    if (stack.length == 0) {
      return -1;
    } else {
      return stack.pop();
    }
  },
  size: () => {
    return stack.length;
  },
  empty: () => {
    if (stack.length == 0) {
      return 1;
    } else {
      return 0;
    }
  },
  top: () => {
    if (stack.length == 0) {
      return -1;
    } else {
      return stack[stack.length - 1];
    }
  },
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const n = Number(input[0]);
  for (let i = 1; i <= n; i++) {
    let commend = input[i].split(" ");
    if (commend[0] == "push") {
      result.push(commend[1]);
    } else if (commend[0] == "pop") {
      console.log(result.pop());
    } else if (commend[0] == "size") {
      console.log(result.size());
    } else if (commend[0] == "empty") {
      console.log(result.empty());
    } else if (commend[0] == "top") {
      console.log(result.top());
    }
  }
  process.exit();
});
