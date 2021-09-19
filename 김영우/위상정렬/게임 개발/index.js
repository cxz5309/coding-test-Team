const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `4
20 -1
10 -1
1 1 2 -1
1000 3 -1`
).split('\n');
 
let n;

n = Number(stdin[0]);
stdin.shift();

let graph = Array.from(Array(n+1), ()=> Array().fill([]));
let visited = Array(n+1).fill(false);

for(let i=0;i<n;i++){
  const line = stdin[i].split(' ').map(Number);
  const idx = i+1;
  const time = line[0];

  const model = {'node': idx, 'time': time}

  if(line.length-2 === 0)
    graph[0].push(model);

  for(let j=1; j<line.length-1; j++){
    const parentIdx = line[j];
    graph[parentIdx].push(model);
  }
}
let dp = Array(n+1).fill(0);

// console.log(graph);

//--------------------------------------------------------

let stack = [];

const DFS = (now)=>{
  const nowNode = now['node'];
  const nowTime = now['time'];

  dp[nowNode] += nowTime;
  
  console.log(nowNode);


  for(let next of graph[nowNode]){
    //  console.log(next);
    const nextNode = next['node']
    const nextTime = next['time']

    if(visited[nextNode]) continue;
    visited[nextNode] = true;
    DFS(next);
  }
  stack.push(nowNode);
}

function solution(){
    let answer = [];
    for(let i=0;i<=n;i++){
      stack = [];
      for(let val of graph[i]){
        console.log('node' + val['node']);
        DFS(val);
      }
      console.log(stack);
    }
    // answer = dp.filter((val, idx)=>idx>0);
    return answer;
}


console.log(solution().join('\n'));