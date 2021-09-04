const fs = require('fs');
const stdin = (process.platform === 'linux'
? fs.readFileSync('/dev/stdin').toString()
: `5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10`
).split('\n');
 
let n, m;
let cards = [];
let nums = [];

n = Number(stdin[0]);
stdin.shift();

cards = stdin[0].split(' ').map(Number);
stdin.shift();

m = Number(stdin[0]);
stdin.shift();

nums = stdin[0].split(' ').map(Number);
stdin.shift();


//--------------------------------------------------------

const binarySearch = (arr, start, end, find)=>{
  while(start<=end){
    const middle = Math.floor((end + start) / 2);
    if(arr[middle] === find){
      return 1;
    }
    else if(arr[middle]<find){
      start = middle + 1;
    }
    else{
      end = middle - 1;
    }
  }
  return 0;
}

function solution(n,m,cards,nums){
    let answer = [];
    cards.sort((a,b)=>{
      return a-b;
    })
    // console.log(cards);
    // console.log(nums);
    for(let num of nums){
      answer.push(binarySearch(cards, 0, n-1, num));
    }
    return answer;
}


console.log(solution(n,m,cards,nums).join(' '));