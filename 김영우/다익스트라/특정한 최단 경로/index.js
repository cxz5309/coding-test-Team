const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
const input = [];
const graph = [];

const dijkstra = (graph, start) => {
    const distances = [];
    const visited = [];
    for (let i = 0; i < graph.length; i++) distances[i] = Number.MAX_VALUE;
    distances[start] = 0;
    while (true) {
        let shortestDist = Number.MAX_VALUE;
        let shortestIndx = -1;
        for (let i = 0; i < graph.length; i++) {
            if (distances[i] < shortestDist && !visited[i]) {
                shortestDist = distances[i];
                shortestIndx = i;
            }
        }
        if (shortestIndx === -1) return distances;
        for (let i = 0; i < graph[shortestIndx].length; i++) {
            if (graph[shortestIndx][i] !== 0 && distances[i] > distances[shortestIndx] + graph[shortestIndx][i]) {
                distances[i] = distances[shortestIndx] + graph[shortestIndx][i];
            }
        }
        visited[shortestIndx] = true;
    }
}

rl.on('line', line => input.push(line)).on('close', () => {
    let [N, E] = input[0].split(' ').map(ele => parseInt(ele));
    for (let i = 1; i <= N; i++) {
        graph[i] = [];
        for (let j = 1; j <= N; j++) {
            graph[i][j] = 0;
        }
    }
    for (let i = 1; i <= E; i++) {
        let [a, b, c] = input[i].split(' ').map(ele => parseInt(ele));
        graph[a][b] = graph[b][a] = c;
    }
    const [v1, v2] = input[E+1].split(' ').map(ele => parseInt(ele));

    const distFromOne = dijkstra(graph, 1);
    const distFromV = dijkstra(graph, v1);
    const distFromN = dijkstra(graph, N);

    const d1 = distFromOne[v1] + distFromV[v2] + distFromN[v2];
    const d2 = distFromOne[v2] + distFromV[v2] + distFromN[v1];
        
    let result = Math.min(d1, d2);
    if (result >= Number.MAX_VALUE) result = -1;
    console.log(result);
})
