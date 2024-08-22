```js
function solution(s) {
  let answer = 1;
  s = s.split("");
  let first_length = s.length;
  while (s.length > 1) {
    for (let i = 0; i < s.length - 1; i++) {
      // 제거 조건
      if (s[i] == s[i + 1]) {
        s.splice(i, 2);
        break;
      }
    }
    // 더 이상 제거할 수 없을 때
    if (first_length == s.length) {
      answer = 0;
      break;
    }
  }
  return answer;
}
```

- 최초로 실행한 코드이다. 하지만 시간제한에 걸려 실패했다.
- stack을 사용해서 문제를 풀어보려 한다.

```js
function solution(s) {
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    if (!stack.length || stack[stack.length - 1] !== s[i]) stack.push(s[i]);
    else stack.pop();
  }
  return stack.length === 0 ? 1 : 0;
}
```

- 다음과 같은 방식으로 바꿨다.
- stack에 문자를 넣어주고, 이전의 문자와 같다면 pop을 해준다.
- stack이 비어있다면 answer는 1이 되고, 아니라면 0이 된다.
