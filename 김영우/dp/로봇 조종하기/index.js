const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15`
).split('\n');
 
let n, m;
let nums = [];

n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();


nums.push(Array(m+1).fill(0));
for(let i=0;i<n;i++){
    let arr = [];
    arr = [0, ...stdin[0].split(' ').map(Number)];
    nums.push(arr);
    stdin.shift();
}
console.log(nums);
let dp = Array.from(Array(n+1), ()=>Array(m+1).fill(0));
let temp = Array.from(Array(n+1), ()=>Array.from(Array(m+1), ()=>Array(3).fill(0)));
//--------------------------------------------------------


function solution(){
    let answer;
    dp[1][1] = nums[1][1];
    for (let i = 1; i <= m; i++) 
        dp[1][i] = dp[1][i - 1] + nums[1][i];
    for (let i = 2; i <= n; i++)
    {
        for (let j = 1; j <= m; j++)
        {
            temp[i][j][0] = dp[i - 1][j] + nums[i][j];
            temp[i][j][1] = dp[i - 1][j] + nums[i][j];
        }
        for (let j = 2; j <= m; j++) 
            temp[i][j][0] = Math.max(temp[i][j][0], temp[i][j - 1][0] + nums[i][j]);
        for (let j = m - 1; j >= 1; j--) 
            temp[i][j][1] = Math.max(temp[i][j][1], temp[i][j + 1][1] + nums[i][j]);
        for (let j = 1; j <= m; j++) 
            dp[i][j] = Math.max(temp[i][j][0], temp[i][j][1]);
    }
    console.log(dp);
    answer = dp[n][m];
    return answer;
}


console.log(solution());