```py
function solution(n) {
  let ans = 1;
  while (n !== 1) {
    if (Number.isInteger(n / 2)) {
      n /= 2;
    } else {
      n -= 1;
      ans += 1;
    }
  }
  return ans;
}
```

- 0에서 n을 간다고 생각하지 말고 반대로 n에서 0으로 간다고 생각하면 직관적인 문제다.
- 2의 배수가 나올 때마다 1/2 를 해주는 것은 절반이 되는 경우, 2의 배수가 아닐 때는 -1을 해주어 1/2를 해준다.
- 이렇게 하면 n이 0이 될 때까지 반복하면서 ans를 증가시키면 된다. 이때 ans는 사용한 배터리의 수치이다.
