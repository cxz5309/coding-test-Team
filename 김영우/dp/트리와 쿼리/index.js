const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8`
).split('\n');
 
let n, r, q;
let line = stdin.shift().split(' ').map(Number);
n = line[0];
r = line[1];
q = line[2];

let graph = Array.from(Array(n+1), ()=>new Array());
// console.log(graph);
for(let i=0;i<n-1;i++){
  line = stdin[i].split(' ').map(Number);

  graph[line[0]].push(line[1]);
  graph[line[1]].push(line[0]);
}

//--------------------------------------------------------
let size = Array(n+1).fill(1);
const dfs = (now, prev)=>{
  for(let next of graph[now]){
    if(prev === next) continue;
    size[now] += dfs(next, now);
  }
  return size[now];
}

function solution(){
  let answer = '';
  dfs(r, 0);
  
  for(let i=n-1;i<n - 1 + q;i++){
    answer += size[Number(stdin[i])] + '\n';
  }
  return answer;
}


console.log(solution());