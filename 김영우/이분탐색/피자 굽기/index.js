const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `7 3
5 6 4 3 6 2 3
3 2 5`
).split('\n');
 
const d = Number(stdin[0].split(' ')[0]);
const n = Number(stdin[0].split(' ')[1]);
stdin.shift();

let ovenLen = stdin.shift().split(' ').map(Number);
let min = Infinity;
let newOvenLen = ovenLen.map((val)=>{
  if(val>min) val = min;
  else min = Math.min(min, val);
  return val;
});
const pizzaLen = stdin.shift().split(' ').map(Number);

//--------------------------------------------------------
function binarySearch(sortedArray, startIdx, endIdx, seekElement) {
  while (startIdx < endIdx) {
    const middleIdx = Math.floor((endIdx + startIdx) / 2);
    if (sortedArray[middleIdx] >= seekElement) {
      startIdx = middleIdx + 1;
    } 
    else{
      endIdx = middleIdx;
    }
  }
  return endIdx;
}
function solution(d, n, ovenLen, pizzaLen){
    let answer = 0;
    
    console.log(ovenLen.join(' '));
    let end = d;
    let now = d;
    answer = 0;
    for(let i=0;i<n;i++){
      if(ovenLen[0]<pizzaLen[i])
        return 0;
      now = binarySearch(ovenLen, 0, end, pizzaLen[i]);
      end = now - 1;
      console.log('now' + now);
      if(end<0) break;
    }
    return now;
}

console.log(solution(d, n, newOvenLen, pizzaLen));