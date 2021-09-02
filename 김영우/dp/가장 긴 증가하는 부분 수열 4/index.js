const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `6
10 20 10 30 20 50`
).split('\n');
 

let testCase;

testCase = Number(stdin[0]);
stdin.shift();
const sequence = stdin[0].split(' ').map(Number);

//--------------------------------------------------------

function solution(t, sequence){
  let answer = [];
  let len = 0;
  // console.log(sequence);
  let dp = new Array(t).fill(1);
  for(let i=0; i<t; i++){
      const thisNum = sequence[i];
      for(let j=0; j<i; j++){
          let prev = sequence[j];
          if(thisNum>prev){
              dp[i] = Math.max(dp[i], dp[j] + 1);
          }
      }
      // console.log(dp.join(' '));
      len = Math.max(len, dp[i]);
  }
  for(let i=1;i<=len;i++){
    const idx = dp.findIndex((val)=>val === i);
    answer.push(sequence[idx]);
  }
  console.log(len);
  console.log(answer.join(' '));
}

solution(testCase, sequence);