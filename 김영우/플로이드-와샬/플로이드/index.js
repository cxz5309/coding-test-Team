const fs = require('fs');
const stdin = (process.platform === 'linux' ?
  fs.readFileSync('/dev/stdin').toString() :
  `5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4`
).split('\n');

let n, m;

n = Number(stdin[0]);
stdin.shift();

m = Number(stdin[0]);
stdin.shift();

const arr = Array.from(Array(n + 1), () => Array(n + 1).fill(Infinity));
for (i = 0; i <= n; i++) {
  arr[i][i] = 0;
}

for (let i = 0; i < m; i++) {
  const line = stdin[i].split(' ').map(Number);
  const a = line[0];
  const b = line[1];
  const c = line[2];
  arr[a][b] = Math.min(arr[a][b], c);
}
console.log(arr);
//--------------------------------------------------------

const floyd = () => {
  for (let k = 1; k <= n; k++) {
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        if (arr[i][j] > arr[i][k] + arr[k][j]) {
          arr[i][j] = arr[i][k] + arr[k][j];
        }
      }
    }
  }
}


function solution() {
  let answer = '';
  floyd();

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (arr[i][j] == Infinity) {
        arr[i][j] = 0;
      }

      answer += arr[i][j] + ' ';
    }
    answer += '\n';
  }
  return answer;
}


console.log(solution());