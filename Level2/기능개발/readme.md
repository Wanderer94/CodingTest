```js
function solution(progresses, speeds) {
  var answer = [];
  while (progresses[0]) {
    let count = 0;
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }
    while (progresses[0] > 100) {
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
```

- 통과되었으나 마지막에 실패했다 원인을 파악해보자
- while문 중 progresses[0]이 정확히 100이 될 때 문제가 발생
- 따라서 >=로 경계값을 받아줘서 문제 해결
- 속도에서 개선 사항이 있어 다음과 같이 변경
- loop를 최소화 하는 방식으로 해결

```js
function solution(progresses, speeds) {
  // answer: 각 배포마다 배포되는 기능의 수가 적힌 정수 배열
  var answer = [];
  // days: 배포일
  let days = 1;
  // cnt: 오늘 배포되는 기능의 수
  let cnt = 0;
  // progress: 현재 기능의 작업 진도
  let progress = 0;

  // 모든 작업이 다 배포될 때까지 반복
  while (progresses[0]) {
    // 첫 번째 기능의 작업 진도
    progress = progresses[0] + speeds[0] * days;
    // 첫 번째 기능의 작업 진도가 100 이상인 경우 배포 완료
    if (progress >= 100) {
      // 배포 완료된 기능 개수 추가
      cnt++;
      // 배포 완료된 작업 제거
      progresses.shift();
      // 배포 완료된 작업의 속도 제거
      speeds.shift();
    }
    // 첫 번째 기능의 작업 진도가 100 미만일 경우 배포 불가능
    else {
      // 배포 완료된 기능이 있는 경우, answer에 push
      if (cnt > 0) {
        answer.push(cnt);
      }
      // 배포일 증가 (다음날)
      days++;
      // 배포 완료된 기능 개수 초기화
      cnt = 0;
    }
  }
  // 모든 작업이 다 배포되고 나면, 마지막으로 카운트된 배포 완료 기능 개수 push
  answer.push(cnt);

  return answer;
}
```
