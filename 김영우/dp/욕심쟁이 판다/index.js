const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16`
).split('\n');
 

let n;
let map = [];
n = Number(stdin[0]);
stdin.shift();
let dp = Array.from(Array(n), ()=>Array(n).fill(0));

for(let i=0; i<n; i++){
    let line = stdin[i].split(' ').map(Number);
    map.push(line);
}
// console.log(map);
//--------------------------------------------------------

let moveX = [1, 0, -1, 0];
let moveY = [0, 1, 0, -1];

const range = (x, y)=>{
    return x>=0 && x<n && y>=0 && y<n;
}

let max = 0;

const DFS = (nowX, nowY)=>{
    let nextX, nextY;
    if(dp[nowY][nowX] !== 0) return dp[nowY][nowX];
    dp[nowY][nowX] = 1;

    for(let i=0;i<4;i++){
        nextX = nowX + moveX[i];
        nextY = nowY + moveY[i];
        if(!range(nextX, nextY)) continue;
        if(map[nextY][nextX] <= map[nowY][nowX]) continue;
        // console.log([nextX, nextY]);
        dp[nowY][nowX] = Math.max(dp[nowY][nowX], DFS(nextX, nextY) + 1);
    }
    console.log(dp);
    return dp[nowY][nowX];
}


function solution(n){
    let answer = 0;
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            if(range(j, i+1) && map[i][j] > map[i+1][j]
            || range(j+1, i) && map[i][j] > map[i][j+1]
            || range(j, i-1) && map[i][j] > map[i-1][j]
            || range(j-1, i) && map[i][j] > map[i][j-1]) continue;
            // console.log([j, i]);
            // console.log("!" + d);
            max = Math.max(max, DFS(j, i, 1));
        }
    }
    answer = max;
    return answer;
}


console.log(solution(n));