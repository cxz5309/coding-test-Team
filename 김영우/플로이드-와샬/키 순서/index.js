const fs = require('fs');
const stdin = (process.platform === 'linux' ?
  fs.readFileSync('/dev/stdin').toString() :
  `6 6
1 5
3 4
5 4
4 2
4 6
5 2`
).split('\n');

let n, m;
n = Number(stdin[0].split(' ')[0]);
m = Number(stdin[0].split(' ')[1]);
stdin.shift();

let map = Array.from(Array(n+1), ()=>Array(n+1).fill(0));

for(let i=0;i<m;i++){
  const line = stdin[i].split(' ').map(Number);
  map[line[0]][line[1]] = 1;
}

//--------------------------------------------------------


const floyd = ()=>{
  for (let k = 1; k <= n; k++)
	{
		for (let i = 1; i <= n; i++)
		{
			for (let j = 1; j <= n; j++)
			{
				if (map[i][k] && map[k][j])
					map[i][j] = 1;
			}
		}
	}
}

const canCompare = (student)=>{
  for(let i=1;i<=n;i++){
    if(i===student) continue;
    if(map[student][i] === 0 && map[i][student] === 0)
      return false;
  }
  return true;
}
function solution() {
  let answer = 0;
  
  floyd();
  map.forEach((val)=>{console.log(val.join(' '))});
  for(let i=1;i<=n;i++){
    if(canCompare(i)) answer++;
  }

  return answer;
}


console.log(solution());