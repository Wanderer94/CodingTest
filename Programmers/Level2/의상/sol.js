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
