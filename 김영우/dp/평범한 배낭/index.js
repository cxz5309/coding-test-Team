const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `4 7
6 13
4 8
3 6
5 12`
).split('\n');
 
testCase = Number(stdin[0].split(' ')[0]);
k = Number(stdin[0].split(' ')[1]);
stdin.shift();

let item = [];
item.push(undefined);
for(let i=0; i<testCase; i++){
    item.push(stdin[i].split(' ').map(Number));
}

function solution(n, k, item){
    let answer = [];
    let dp = Array.from(Array(n+1), ()=>Array(k+1).fill(0));
    for(let i=1;i<=n;i++){
        const weight = item[i][0];
        const value = item[i][1];
        for(let j=1;j<=k;j++){
            if(j<weight) 
                dp[i][j] = dp[i-1][j];
            else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-weight] + value);
            }
        }
    }
    answer = dp[n][k];
    return answer;
}


console.log(solution(testCase, k, item));