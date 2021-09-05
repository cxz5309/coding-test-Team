const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `6 2
-1 3 1 2 4 -1`
).split('\n');
 
let n, m;
let nums = [];
n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();

if(stdin[0].split(' ').length>1){
  nums = stdin[0].split(' ').map(Number);
}
else{
  for(let i=0;i<n;i++){
    nums.push(Number(stdin[0]));
    stdin.shift();
  }
}

let dp = Array.from(Array(nums.length+1), ()=>Array(nums.length+1).fill(-40000));

//--------------------------------------------------------

const makeDp=(idx, sec)=>{
  if(sec===0) return 0;
  if(idx<=0) return -Infinity;
  if(dp[idx][sec] !== -40000) return dp[idx][sec];

  dp[idx][sec] = makeDp(idx-1, sec);

  let sum = 0;
  for(let i=idx; i>0; i--){
    sum += nums[i-1];
    dp[idx][sec] = Math.max(dp[idx][sec], makeDp(i-2, sec-1) + sum);
  }

  // console.log('[idx : ' + idx + ' sec : ' + sec + ']');
  // console.log(dp[idx][sec]);
  // for(let i=1;i<dp.length;i++){
  //   console.log(dp[i].filter((val, idx)=>idx>0 && idx<=m).join(' '));
  // }
  return dp[idx][sec];
}

function solution(n,m){
    let answer;

    console.log(nums);
    answer = makeDp(n, m);

    return answer;
}


console.log(solution(n,m));