const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input=[]
rl.on("line",function(line){
    input.push(line)
}).on("close",function(){
    let n = Number(input[0])
    const factorial = (n)=>{
        if(n<=1){
            return 1
        }else{
            return n* factorial(n-1)
        }
    }
    console.log(factorial(n))
})