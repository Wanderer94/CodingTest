function solution(n) {
  var answer = 0;
  var boundary = n / 2 + 1;
  for (let i = 1; i < boundary; i++) {
    var total = 0;
    for (let j = i; j < boundary; j++) {
      total += j;
      if (total > n) {
        break;
      } else if (total == n) {
        answer++;
        break;
      }
    }
  }
  return n == 1 ? 1 : ++answer;
}
