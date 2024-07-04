function solution(cacheSize, cities) {
  // 캐시 크기가 0인 경우 모든 조회가 캐시 실패
  if (cacheSize === 0) return cities.length * 5;

  let answer = 0;
  let cache = [];

  // 대소문자 구분 없이 처리하기 위해 모든 도시 이름을 소문자로 변환
  cities = cities.map((city) => city.toLowerCase());

  for (let city of cities) {
    let index = cache.indexOf(city);

    // 캐시 적중(cache hit)
    if (index !== -1) {
      cache.splice(index, 1); // 기존 위치에서 제거
      cache.push(city); // 가장 최근 사용으로 갱신
      answer += 1;
    } else {
      // 캐시 실패(cache miss)
      if (cache.length >= cacheSize) {
        cache.shift(); // 가장 오래된 항목 제거
      }
      cache.push(city); // 새로운 항목 추가
      answer += 5;
    }
  }

  return answer;
}
