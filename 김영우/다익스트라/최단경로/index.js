const fs = require('fs');
const stdin = (process.platform === 'linux' ?
  fs.readFileSync('/dev/stdin').toString() :
`5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6`
).split('\n');

let V, E, K;

V = Number(stdin[0].split(' ')[0]);
E = Number(stdin[0].split(' ')[1]);
stdin.shift();
K = Number(stdin[0]);
stdin.shift();

let graph =  new Array(V + 1);

for (let i = 0; i < E; i++) {
  const line = stdin[i].split(' ').map(Number);
  const u = line[0];
  const v = line[1];
  const w = line[2];

  if (!graph[u]) graph[u] = []
  graph[u].push({
      vertex: v,
      cost: w
  })
}

//  console.log(graph);

//--------------------------------------------------------
// 우선순위 큐 3번

class MinHeap {
  constructor() {
      this.nodes = []
  }

  insert(value) {
      this.nodes.push(value)
      this.bubbleUp()
  }

  bubbleUp(index = this.nodes.length - 1) {
      if (index < 1) return;

      const currentNode = this.nodes[index]
      const parentIndex = Math.floor((index - 1) / 2)
      const parentNode = this.nodes[parentIndex]
      if (parentNode.cost <= currentNode.cost) return;

      this.nodes[index] = parentNode
      this.nodes[parentIndex] = currentNode
      index = parentIndex
      this.bubbleUp(index)
  }

  extract() {
      const min = this.nodes[0]
      if(this.nodes.length === 1){
          this.nodes.pop();
          return min;
      };
      this.nodes[0] = this.nodes.pop()
      this.trickleDown();
      return min
  }

  trickleDown(index = 0) {
      const leftChildIndex = 2 * index + 1
      const rightChildIndex = 2 * index + 2
      const length = this.nodes.length
      let minimum = index

      if(!this.nodes[rightChildIndex] && !this.nodes[leftChildIndex]) return;
      if(!this.nodes[rightChildIndex]){
          if(this.nodes[leftChildIndex].cost < this.nodes[minimum].cost){
              minimum = leftChildIndex;
          }
          return;
      }

      if(this.nodes[leftChildIndex].cost > this.nodes[rightChildIndex].cost){
          if (rightChildIndex <= length && this.nodes[rightChildIndex].cost < this.nodes[minimum].cost) {
              minimum = rightChildIndex
          }
      }else{
          if (leftChildIndex <= length && this.nodes[leftChildIndex].cost < this.nodes[minimum].cost) {
              minimum = leftChildIndex
          }
      }

      if (minimum !== index) {
          let t = this.nodes[minimum]
          this.nodes[minimum] = this.nodes[index]
          this.nodes[index] = t
          this.trickleDown(minimum)
      }
  }
}


let startToEnd = Array(V + 1).fill(Infinity);

const dijkstra=(start)=>{
  const q = new MinHeap();
  q.insert({vertex: start, cost: 0})
  startToEnd[start] = 0;
  startToEnd[0] = -1;
  console.log(q.nodes);

  while(q.nodes.length > 0){
    console.log(q.nodes);
    const now = q.extract();
    
    console.log(startToEnd)
    if(startToEnd[now.vertex] < now.cost) continue;
    if(!graph[now.vertex]) continue;//??
    graph[now.vertex].forEach((next)=>{
      const {vertex, cost} = next
      if(startToEnd[vertex] <= startToEnd[now.vertex] + cost)
        return;
      startToEnd[vertex] = startToEnd[now.vertex] + cost;
      const newNext = {
        vertex,
        cost: startToEnd[now.vertex] + cost
      };//??
      q.insert(newNext);
    });
  }
}

function solution(K) {
  let answer = "";
  dijkstra(K);

  startToEnd.forEach((val, idx)=>{
    if(idx === 0) return;
    if(val === Infinity) {
      answer += 'INF\n';
      return;
    }
    answer += val + '\n';
  });
  return answer;
}


console.log(solution(K, graph));