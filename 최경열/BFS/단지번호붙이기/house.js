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
    const dx = [0, 0, -1, 1]
    const dy = [-1, 1, 0, 0]

    for(let i=1; i<=n; i++){
        graph.push(input[i].split("").map(Number));
    }
    function bfs(x,y){
        const queue = []
        queue.push([x,y])
        graph[x][y]=0
        let count=1
        while(queue.length){
            const target =queue.shift()
            x=target[0]
            y=target[1]
            for(let i=0; i<4; i++){
                nx = x+ dx[i]
                ny = y+ dy[i]
                if(nx <= -1 || nx >= n || ny <= -1 || ny >= n){
                    continue
                }
                if(graph[nx][ny]==1){
                    graph[nx][ny] = 0
                    queue.push([nx, ny])
                    count += 1
                }
            }
        }
        return count
    }

    for(let i =0; i<n; i++){
        for(let j=0; j<n; j++){
            if(graph[i][j] == 1){
                arr.push(bfs(i, j))
            }
        }
    }
    
    arr.sort((a,b)=>a-b)
    console.log(arr.length)

    for(let i in arr){
        console.log(arr[i])
    }
})