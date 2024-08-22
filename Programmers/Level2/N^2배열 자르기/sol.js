function solution(n, left, right) {
  var answer = [];
  for (let i = left; i <= right; i++) {
    col = parseInt(i / n);
    row = i % n;
    answer.push(Math.max(col, row) + 1);
  }
  return answer;
}
