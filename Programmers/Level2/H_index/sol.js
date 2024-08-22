function solution(citations) {
  var answer = 0;
  let n = citations.length;
  for (let i = 1; i <= n; i++) {
    let h_cita = citations.filter((citation) => citation >= i);
    if (h_cita.length >= i) answer = i;
  }
  return answer;
}
