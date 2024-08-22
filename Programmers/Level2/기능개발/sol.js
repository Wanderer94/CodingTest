function solution(progresses, speeds) {
  var answer = [];
  while (progresses[0]) {
    let count = 0;
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }
    while (progresses[0] >= 100) {
      progresses.shift();
      speeds.shift();
      count += 1;
    }
    if (count > 0) {
      answer.push(count);
    }
  }
  return answer;
}
