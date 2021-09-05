const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `8 4
-1
-1
1
1
1
1
-1
2`
).split('\n');
 
let n, m;

n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();

let dp = Array(n + 1).fill(0);

for(let i=0;i<n;++i){
  dp[i + 1] = dp[i] + Number(stdin[i]);
}

//--------------------------------------------------------

function solution(n,m){
    let answer = 0;
    let prev = 0;
    console.log(dp);
    for(let i=m-1; i<n; ++i){
      prev = Math.min(prev, dp[i-m+1]);
      answer = Math.max(answer, dp[i+1] - prev)
      console.log('prev : ' + (i-m+1));
      console.log('now : ' + (i+1));
      console.log(answer);
    }
    return answer;
}


console.log(solution(n,m));