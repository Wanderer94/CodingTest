```js
function solution(s) {
  var answer = [];
  let temp_list = [];
  let temp = "";
  // 양쪽 {}를 제거
  s = s.slice(1, s.length - 1);
  //{ 이 시작되면 str에 전부 집어 넣기, }나오면 close 하고 str을 split 해서 set에 넣기
  for (let string in s) {
    if (string === "{") {
      temp = "";
    } else if (string === "}") {
      temp_list.push(temp);
    } else {
      temp += string;
    }
  }
  return answer;
}
```

- 위 토드의 문제는 하나씩 문자열을 받아들여서 한자리수 이상의 숫자에 대해서 문제가 발생한다.

- 다음과 같이 json의 특징을 살려서 기능을 구현했다.

```js
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
```
