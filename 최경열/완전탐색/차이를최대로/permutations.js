const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {

const n =Number(input[0])
const arr = input[1].split(" ");
let check = [];
let selected = [];
let result = 0;
//최대값
function checkMax(check_arr){
  var sum = 0;

  for(let j=1;j<n;++j){
      sum += Math.abs(check_arr[j]-check_arr[j-1]);
  }
  result = Math.max(sum,result);
}

//순열
function permutations(depth){
  if(depth === n) {   
      checkMax(selected);
  }
  for(var i = 0; i<n; ++i){
      if(check[i]){
        continue
      }
      check[i] = true;
      selected[depth] = arr[i];
      permutations(depth+1);
      check[i] = false;
  }
}
permutations(0);
console.log(result);
});
