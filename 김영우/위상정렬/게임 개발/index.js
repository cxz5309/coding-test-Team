const fs = require('fs');
const stdin = (process.platform === 'linux' ?
  fs.readFileSync('/dev/stdin').toString() :
`6
10 -1
10 1 6 -1
4 1 -1
4 3 1 -1
3 3 -1
9 -1`
).split('\n');

let n;

n = Number(stdin[0]);
stdin.shift();

let graph = Array.from(Array(n + 1), () => Array().fill([]));
let indegree = Array(n + 1).fill(0);
let q = [];

for (let i = 0; i < n; i++) {
  const line = stdin[i].split(' ').map(Number);
  const idx = i + 1;
  const time = line[0];

  const model = {
    'node': idx,
    'time': time
  }

  indegree[idx] = line.length - 2;
  if (indegree[idx] === 0) {
    graph[0].push(model);
  }
  for (let j = 1; j < line.length - 1; j++) {
    const parentIdx = line[j];
    graph[parentIdx].push(model);
  }
}
let dp = Array(n + 1).fill(0);

// console.log(graph);

//--------------------------------------------------------


function solution() {
  let answer = [];

  for (let node of graph[0]) {
    dp[node['node']] = 0;
    q.push(node);
    dp[node['node']] = node['time'];
  }

  while (q.length > 0) {
    const now = q.shift();
    const nowNode = now['node'];
    const nowTime = now['time'];

    // console.log("nowNode" + nowNode);
    for (let next of graph[nowNode]) {
      const nextNode = next['node'];
      const nextTime = next['time'];
      // console.log(nextNode);
      if (dp[nextNode] < dp[nowNode] + nextTime) {
        dp[nextNode] = dp[nowNode] + nextTime;
      }

      indegree[nextNode]--;
      if (indegree[nextNode] === 0)
        q.push(next);
    }
  }
  answer = dp.filter((val, idx) => idx > 0);
  return answer;
}


console.log(solution().join('\n'));