const readline = require("readline");
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout 
})
let input=[]
rl.on("line",function(line){
    input.push(line)
}).on("close",function(){
    let a=Number(input[0])
    let word = input[1].split("")
    let arr=[]
    let stack =[]
    for(let i=2; i<a+2; i++){
        arr.push(Number(input[i]))
    }
    word.map((value)=>{
        if(value.match(/^[A-Z]/g)){
            stack.push(arr[value.charCodeAt(0)-'A'.charCodeAt(0)])
        }else{
            x = stack.pop()
            y= stack.pop()
            if(value=="+"){
                stack.push(y+x)
            }else if(value=="-"){
                stack.push(y-x)
            }else if(value =="*"){
                stack.push(y*x)
            }else if(value=="/"){
                stack.push(y/x)
            }
        }
    })
    console.log(stack[0].toFixed(2))
})