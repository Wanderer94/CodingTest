```js
function solution(citations) {
  var answer = 0;
  let n = citations.length;
  for (let i = 1; i <= n; i++) {
    let h_cita = citations.filter((citation) => citation >= i);
    if (h_cita.length >= i) answer = i;
  }
  return answer;
}
```

- H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

- 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

- 따라서 위의 조건을 만족하는 수를 파악하면 된다.
- H-Index의 경우 1부터 n까지의 범위를 가지므로, for문을 사용하여 1부터 n까지 반복하며, citations 배열에서 h번 이상 인용된 논문이 h편 이상인지 확인한다. 만약 해당 조건을 만족하는 수가 나오면 answer에 h를 저장하고 다음 비교를 진행한다.
