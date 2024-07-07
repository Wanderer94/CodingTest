```js
function solution(clothes) {
  // 의상의 종류별로 의상 수를 계산
  const clothesMap = new Map();
  for (let [name, type] of clothes) {
    if (clothesMap.has(type)) {
      clothesMap.set(type, clothesMap.get(type) + 1);
    } else {
      clothesMap.set(type, 1);
    }
  }

  // 모든 조합의 수 계산 (의상을 입지 않은 경우 포함)
  let answer = 1;
  for (let count of clothesMap.values()) {
    answer *= count + 1;
  }

  // 아무것도 입지 않은 경우 제외
  return answer - 1;
}
```
- 어렵게 접근했지만 그림으로 케이스를 나누어 보면 쉬웠던 구현문제
- 의상 종류별로 생각해보면 쉽다. 안입는것을 포함한 경우를 생각해 조합을 구한다.
- 이후 최종적으로 아무것도 입지 않은 케이스에 대해서만 빼주면 완료