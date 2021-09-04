const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `6
1 3 5 7 2 3`
).split('\n');
 

let testCase;

testCase = Number(stdin[0]);
stdin.shift();
const seq = stdin[0].split(' ').map(Number);

//--------------------------------------------------------

function solution(t, seq){
  let dp = new Array(t).fill(1);
  let dpNums = [];
  let dpMax = 0;
  for(let i=0; i<t; i++){
      const thisNum = seq[i];
      for(let j=0; j<i; j++){
          let prev = seq[j];
          if(thisNum>prev){
              dp[i] = Math.max(dp[i], dp[j] + 1);
          }
      }
      // console.log(dp.join(' '));
      dpMax = Math.max(dpMax, dp[i]);
  }
  let j = seq.length;
  for(let i=dpMax;i>=1;i--){
    while(j>0){
      j--;
      if(dp[j] === i){
        dpNums.unshift(seq[j]);
        break;
      }
    }
  }
  console.log(dpMax);
  console.log(dpNums.join(' '));
}


solution(testCase, seq);