const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync('/dev/stdin').toString()
    : `4 3
1 2 3
6 5 4
7 8 9
12 11 10`
).split('\n');
 
let map = [];

let height = Number(stdin[0].split(' ')[0]);
let width = Number(stdin[0].split(' ')[1]);
stdin.shift();

stdin.forEach((val)=>{
    map.push(val.split(' ').map(Number));
});

//--------------------------------------------------------

function solution(w, h, map){
    let answer = 0;
    for(let i=0;i<h;i++){
        for(let j=0;j<w;j++){
            const prevY = i-1 < 0 ? 0 : map[i-1][j];
            const prevX = j-1 < 0 ? 0 : map[i][j-1];
            map[i][j] += Math.max(prevY, prevX);
        }
    }
    answer = map[h-1][w-1];
    return answer;
}


console.log(solution(width, height, map));