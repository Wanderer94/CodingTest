```js
function solution(priorities, location) {
  var answer = 0;
  let queue = Array.from({ length: priorities.length }, (v, i) => i);
  while (queue) {
    console.log(queue);

    // process에 입력
    let process = queue[0];
    queue.shift();
    let process_pr = priorities[0];
    priorities.shift();
    for (let i = 0; i < priorities.length; i++) {
      // 우선순위 비교
      if (process_pr < priorities[i]) {
        queue.push(process);
        priorities.push(process_pr);
        process = queue[0];
        queue.shift();
        process_pr = priorities[0];
        priorities.shift();
      }
      answer += 1;
    }

    // location과 비교
    if (process === location) break;
  }
  return answer;
}
```
- 프로세스의 동작 방식에 대해서 생각해보면 쉬운 문제였다.
- 핵심은 우선순위가 가장 높은지에 대해서만 작성해보면 된다.
- 수도코드로 먼저 작성해보면 쉬웠을 문제

```js
function solution(priorities, location) {
  let answer = 0;
  let arr = [];
  let max_value = Math.max(...priorities);

  //위치 배열 만들기
  for (let i = 0; i < priorities.length; i++) {
    arr.push(i);
  }

  //priorities 배열이 비어있을 때까지 반복
  while (priorities.length != 0) {
    max_value = Math.max(...priorities);

    if (priorities[0] < max_value) {
      priorities.push(priorities.shift());
      arr.push(arr.shift());
    } else {
      answer += 1;
      priorities.shift();
      if (arr.shift() == location) return answer;
    }
  }
}
```
