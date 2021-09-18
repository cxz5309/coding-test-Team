const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `3 3
1 3
1 2
2 3`
).split('\n');
 
let n, m;
let graph = new Array(32001).fill([]);
let q = [];
n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();

let indegree = Array(n+1).fill(0);

for(let i=0;i<m;i++){
  const line = stdin[i].split(' ').map(Number);

  indegree[line[1]]++;
  graph[line[0]].push(line[1]);
}






//--------------------------------------------------------

function solution(){
    let answer;
    for (let i = 1; i <= n; i++) {
      if (indegree[i]>0) {
          q.push(i);
      }
    }
    
    while(q.length>0) {
      let temp = q.shift();
     
      console.log(temp);
    
      for (i = 0; i < graph[temp].length; i++) {
          indegree[graph[temp][i]]--;
          if (indegree[graph[temp][i]]>0) 
            q.push(graph[temp][i]);
      }
    }
    return answer;
}


console.log(solution());