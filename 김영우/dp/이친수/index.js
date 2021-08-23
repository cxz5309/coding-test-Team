const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `90`
);
 

const n = Number(stdin);
//--------------------------------------------------------

//let cnt = 0;
// const DFS = (now, depth, n)=>{
//     if(depth === n){
//         cnt++;
//         return;
//     }
//     if(now === 0) {
//         DFS(0, depth + 1, n);
//         DFS(1, depth + 1, n);
//     }
//     else{
//         DFS(0, depth + 1, n);
//     }
//     return cnt;
// }

function solution(n){
    let answer = 0;
    //answer = DFS(0, 2, n);

    let bynary = [BigInt(1), BigInt(1)];
    for(let i=2;i<n;i++){
        bynary.push(bynary[i-1] + bynary[i-2]);
    }

    answer = bynary[n-1].toString().replace('n', '');
    return answer;
}

console.log(solution(n));