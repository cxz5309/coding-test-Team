const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `4 4
1 2
2 3
4 1
4 2`
).split('\n');
 
let n, m;
let q = [];
n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();

let graph = Array.from(Array(n+1), () => []);
let indegree = Array(n+1).fill(0);

for(let i=0;i<m;i++){
  const line = stdin[i].split(' ').map(Number);

  indegree[line[1]]++;
  graph[line[0]].push(line[1]);
}

// console.log(indegree);
// console.log(graph);

//--------------------------------------------------------

function solution(){
    let answer = [];
    for (let i = 1; i <= n; i++) {
      if (indegree[i]===0) {
          q.push(i);
      }
    }

    while(q.length>0) {
      let temp = q.shift();
     
      answer.push(temp);
    
      for (let i = 0; i < graph[temp].length; i++) {
          indegree[graph[temp][i]]--;
          if (indegree[graph[temp][i]]===0) 
            q.push(graph[temp][i]);
      }
    }
    return answer;
}


console.log(solution().join(' '));