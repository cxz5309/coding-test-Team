const readline =require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input=[]
rl.on("line",function(line){
    input.push(line)
}).on("close",function(){
    const n = Number(input[0])
    const graph=[]
    const arr=[]
    let count =0
    let result=0
    for(let i=1; i<=n; i++){
        graph.push(input[i].split("").map(Number));
    }
    function dfs(x,y){
        if(x <= -1 || x >= n || y <= -1 || y >= n) return false;
        if(graph[x][y]==1){
            graph[x][y]=0
            count+=1
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            return true
        }
        return false
    }

    for(let i =0; i<n; i++){
        for(let j=0; j<n; j++){
            if(dfs(i,j)==true){
                result+=1
                arr.push(count)
                count=0
            }
        }
    }
    
    arr.sort((a,b)=>a-b)
    console.log(result)

    for(let i in arr){
        console.log(arr[i])
    }
})