function solution(s) {
  var answer = [];

  // 중괄호({})를 대괄호([])로 replace() 후 JSON 파싱
  // 이후 배열길이 순서로 오름차순 정렬
  const tuples = JSON.parse(s.replace(/{/g, "[").replace(/}/g, "]")).sort(
    (a, b) => a.length - b.length
  );
  let set = new Set();
  for (let tuple of tuples) {
    for (let v of tuple) {
      if (!set.has(v)) {
        set.add(v);
        answer.push(v);
      }
    }
  }
  return answer;
}
