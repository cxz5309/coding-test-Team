```js
const fs = require("fs");
const stdin = (
	process.platform === "linux"
		? fs.readFileSync("/dev/stdin").toString()
		: `5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR`
).split("\n");

const getLine = (() => {
	let line = 0;
	return () => stdin[line++];
})();

let n; // 상자의 가로 칸의 수
let graph = [];
let visited = [];

const input = () => {
	n = Number(getLine());
	for (let i = 0; i < n; ++i) {
		graph.push(getLine().split(""));
	}
	visited = Array.from(Array(n), () => Array(n).fill(false));
};
// 상, 하, 좌, 우
let dx = [0, 0, -1, 1];
let dy = [1, -1, 0, 0];

let q = [];
let count = 1;
let ret = [];
function bfs(isRedGreenMedicine, y, x) {
	// 매개변수로 적록색약인지, 아닌지 확인

	// 적록색약이 아니라면?
	if (isRedGreenMedicine == true) {
		if (visited[y][x]) {
			return;
		}

		visited[y][x] = true;
		ret.push(count);

		let cur;
		q.push([y, x]);
		while (q.length != 0) {
			cur = q.shift();

			let y = cur[0];
			let x = cur[1];

			for (let i = 0; i < 4; ++i) {
				let ny = y + dy[i];
				let nx = x + dx[i];

				// 그래프 밖을 벗어나면 continue
				if (ny >= n || ny < 0 || nx >= n || nx < 0) {
					continue;
				}
				// 방문했으면 continue
				if (visited[ny][nx]) {
					continue;
				}

				// 현재 색이랑 다음 색이랑 같으면 q에 넣어줘
				if (graph[ny][nx] == graph[y][x]) {
					visited[ny][nx] = true;
					q.push([ny, nx]);
				}
			}
		}
	} // 적록색약이라면?
	else {
		if (visited[y][x]) {
			return;
		}

		visited[y][x] = true;
		ret.push(count);

		let cur;
		q.push([y, x]);
		while (q.length != 0) {
			cur = q.shift();

			let y = cur[0];
			let x = cur[1];

			for (let i = 0; i < 4; ++i) {
				let ny = y + dy[i];
				let nx = x + dx[i];

				// 그래프 밖을 벗어나면 continue
				if (ny >= n || ny < 0 || nx >= n || nx < 0) {
					continue;
				}
				// 방문했으면 continue
				if (visited[ny][nx]) {
					continue;
				}

				// 현재 색이랑 다음 색이랑 같으면 q에 넣어줘
				if (graph[ny][nx] == "R" && graph[y][x] == "G") {
					visited[ny][nx] = true;
					q.push([ny, nx]);
				} else if (graph[ny][nx] == "G" && graph[y][x] == "R") {
					visited[ny][nx] = true;
					q.push([ny, nx]);
				} else if (graph[ny][nx] == graph[y][x]) {
					visited[ny][nx] = true;
					q.push([ny, nx]);
				}
			}
		}
	}
}

const solve = () => {
	let result = [];
	for (let i = 0; i < n; ++i) {
		for (let j = 0; j < n; ++j) {
			if (visited[i][j] == false) {
				bfs(true, i, j);
				count++;
			}
		}
	}
	result.push(ret.length);

	ret = [];
	q = [];
	count = 1;
	visited = Array.from(Array(n), () => Array(n).fill(false));

	for (let i = 0; i < n; ++i) {
		for (let j = 0; j < n; ++j) {
			if (visited[i][j] == false) {
				bfs(false, i, j);
				count++;
			}
		}
	}
	result.push(ret.length);

	console.log(result.join(" "));
};

const main = () => {
	input();
	solve();
};

main();
```
