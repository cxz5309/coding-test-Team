const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const n = input[0].split(" ").map(Number);
  const R = n[0];
  const C = n[1];
  let graph = [];
  for (let i = 1; i <= R; i++) {
    graph.push(input[i].split("").map((value) => value.charCodeAt(0) - 65));
  }
  let arr = Array(26).fill(0);
  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  function dfs(x, y, z) {
    answer = Math.max(answer, z);
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
        continue;
      }
      if (arr[graph[nx][ny]] == 0) {
        arr[graph[nx][ny]] = 1;
        dfs(nx, ny, z + 1);
        arr[graph[nx][ny]] = 0;
      }
    }
  }
  let answer = 1;
  arr[graph[0][0]] = 1;
  dfs(0, 0, answer);
  console.log(answer);
});
