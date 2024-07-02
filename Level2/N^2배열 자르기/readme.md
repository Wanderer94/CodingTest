```js
function solution(n, left, right) {
  var answer = [];
  let col = 0;
  let row = 0;
  let arr = new Array(n ** 2).fill(0);
  for (let i = 0; i < n ** 2; i++) {
    col = parseInt(i / n);
    row = i % n;
    arr[i] = Math.max(col, row) + 1;
  }
  answer = arr.slice(left, right + 1);
  return answer;
}
```

- 다음과 같이 풀었는데 문제가 발생했다.
- 런타임 오류가 나 힌트를 확인해 보았더니 다음과 같은 문제가 있었다.
- 조건을 확인해보니 left와 right를 활용해주면 되는 문제였다.

```js
function solution(n, left, right) {
  var answer = [];
  for (let i = left; i < right; i++) {
    col = parseInt(i / n);
    row = i % n;
    answer.push(Math.max(col, row) + 1));
  }
  return answer;
}
```
