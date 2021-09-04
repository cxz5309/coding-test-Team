const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `6
10 20 10 30 20 50`
).split('\n');
 

let testCase;
let sequence = [];

testCase = Number(stdin[0]);
stdin.shift();
const lineSplit = stdin[0].split(' ');

for(let i=0; i<testCase; i++){
    sequence.push(Number(lineSplit[i]));
}

//--------------------------------------------------------

function solution(t, sequence){
    let answer = 1;
    console.log(sequence);
    let dp = new Array(t).fill(1);
    for(let i=0; i<t; i++){
        const thisNum = sequence[i];
        for(let j=0; j<i; j++){
            let prev = sequence[j];
            if(thisNum>prev){
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        console.log(dp.join(' '));
        answer = Math.max(answer, dp[i]);
    }
    console.log(dp.join(' '));
    return answer;
}


console.log(solution(testCase, sequence));