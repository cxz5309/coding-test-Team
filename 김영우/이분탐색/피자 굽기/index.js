const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `7 7
5 6 4 3 6 2 1
2 2 3 3 4 5 5`
).split('\n');
 
const d = Number(stdin[0].split(' ')[0]);
const n = Number(stdin[0].split(' ')[1]);
stdin.shift();

let ovenLen = stdin.shift().split(' ').map(Number);
let newOvenLen = ovenLen.map((val, idx)=>{
  if(idx>0)
    if(val>ovenLen[idx-1]) return ovenLen[idx-1];
  return Number(val);
});
const pizzaLen = stdin.shift().split(' ').map(Number);

//--------------------------------------------------------
function binarySearch(sortedArray, startIdx, endIdx, seekElement) {
  let tmpIs = false;
  while (startIdx < endIdx) {
    const middleIdx = Math.floor((startIdx + endIdx) / 2);
    if (sortedArray[middleIdx] >= seekElement) {
      startIdx = middleIdx + 1;
    } 
    else{
      endIdx = middleIdx;
      tmpIs = true;
    }
  }
  if (endIdx === sortedArray.length-1 && tmpIs) return endIdx + 1;
  return endIdx;
}
function solution(d, n, ovenLen, pizzaLen){
    let answer = 0;
    
    console.log(ovenLen);
    let end = d - 1;
    let now = d;
    answer = 0;
    for(let i=0;i<n;i++){
      if(ovenLen[0]<pizzaLen[i])
        return 0;
      now = binarySearch(ovenLen, 0, end, pizzaLen[i]);
      end = now>end ? end : now-1;
      if(now<0) return 0;
      console.log('now' + now);
      console.log('end' + end);
    }
    return now - 1;
}

console.log(solution(d, n, newOvenLen, pizzaLen));