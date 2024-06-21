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

function solution(n) {
  let fibonacci = [0, 1];
  for (let i = 2; i <= n; i++)
    fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 1234567;
  return fibonacci[n];
}
