const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `6
4 3
2 3
1 2
5 4
5 6`
).split('\n');
 
const n = Number(stdin[0]);
stdin.shift();

let graph = Array.from(Array(n+1), ()=>new Array());
for(let i=0; i<stdin.length; i++){
  const line = stdin[i].split(' ').map(Number);
  const a = line[0];
  const b = line[1];
  graph[a].push(b);
  graph[b].push(a);
}
//--------------------------------------------------------

let visited = Array(n+1).fill(false);

const DFS = (now, early) =>{
  let cnt = 0;
  // console.log(now)
  // console.log(early)
  // console.log(graph[now])
  for(let next of graph[now]){
    if(visited[next]) continue;
    visited[next] = true;
    if(early){
      let cnt1 = DFS(next, true);
      let cnt2 = DFS(next, false);

      cnt += Math.min(cnt1, cnt2);
    }
    else{
      visited[next] = true;
      cnt += DFS(next, true)
    }
    visited[next] = false;
  }
  // console.log(cnt);
  // console.log('now: ' + now)
  // console.log('early: ' + early)

  return early === true ? cnt + 1 : cnt;
}

function solution(){
    let answer = Infinity;
    visited[1] = true;
    answer = Math.min(answer, DFS(1, true));
    answer = Math.min(answer, DFS(1, false));

    return answer;
}


console.log(solution());