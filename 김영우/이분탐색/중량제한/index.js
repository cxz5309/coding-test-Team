const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `6 9
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
6 3`
).split('\n');
 
let n, m;

n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();
let maxCost = 0;

let map = new Map();
for(let i=0;i<m;i++){
  let line = stdin[i].split(' ').map(Number);
  const a = line[0];
  const b = line[1];
  const value = line[2];
  if(map.has(a)&&map.get(a).has(b)){
    if(map.get(a).get(b)>value){
      continue;
    }
  }
  let inner = new Map();
  if(map.has(a)){
    inner = map.get(a);
  }
  inner.set(b, value)
  let inner1 = new Map();
  if(map.has(b)){
    inner1 = map.get(b);
  }
  inner1.set(a,value);

  map.set(a, inner);
  map.set(b, inner1);
  maxCost = Math.max(maxCost, value);
}

let start = Number(stdin[m].split(' ')[0]);
let end = Number(stdin[m].split(' ')[1]);
console.log(map);

//--------------------------------------------------------
let visited = new Array(100001).fill(false);
const BFS = (start, end, cost) =>{
  let unVisited = [start];
  visited[start] = true;
  while(unVisited.length>0){
    console.log(unVisited);

    let now = unVisited.shift();
    if(now === end)
      return true;
    console.log(now);
    console.log(map.get(now));

    map.get(now).forEach((value, key)=>{
      if(!visited[key] && cost <= value){
        visited[key] = true;
        unVisited.push(key);
      }
    })
  }
}

const binarySearch = (low, high)=>{
  while(low<=high){
    visited = new Array(100001).fill(false);

    const middle = Math.floor((high + low) / 2);
    if(BFS(start, end, middle)){
      low = middle + 1;
    }
    else{
      high = middle - 1;
    }
  }
  return high;
}

function solution(maxCost){
    let answer;
    answer = binarySearch(0, maxCost);
    return answer;
}

console.log(solution(maxCost));