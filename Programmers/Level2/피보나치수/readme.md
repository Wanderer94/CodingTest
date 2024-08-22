```js
function solution(n) {
  let memo = [0, 1];
  function fibo(n) {
    if (n == 0) {
      return 0;
    } else if (n == 1) {
      return 1;
    } else {
      return fibo(n - 1) + fibo(n - 2);
    }
  }
  return answer;
}
```

- 위의 방식으로 풀었더니 중간부터 에러가 났다
- memoization을 사용해서 다시 해결해보자

```js
function solution(n) {
  let fibonacci = [0, 1];
  for (let i = 2; i <= n; i++)
    fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 1234567;
  return fibonacci[n];
}
```

- 훨씬 코드가 간결해 진것을 볼 수 있다.
