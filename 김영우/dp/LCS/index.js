const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `ACAYKP
CAPCAK`
).split('\n');
 
var str1, str2;

str1 = stdin[0];
stdin.shift();
str2 = stdin[0];
stdin.shift();

//--------------------------------------------------------

function solution(str1, str2){
    let answer;
    const len1 = str1.length;
    const len2 = str2.length;
    const dp = Array.from(Array(len1 + 1), () => Array(len2 + 1).fill(0)); 
    // console.log(dp);

    for(let i = 1; i <= len1; i++) { 
        for(let j = 1; j <= len2; j++) { 
            if(str1.charAt(i - 1) === str2.charAt(j - 1)) 
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else 
                dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]) 
        } 
    } 
    console.log(dp);

    answer = dp[len1][len2];
    return answer;
}


console.log(solution(str1, str2));