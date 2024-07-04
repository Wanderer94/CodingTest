```js
function solution(arr1, arr2) {
  const newArr = [];
  for (let i = 0; i < arr1.length; i++) {
    let result = [];
    for (let j = 0; j < arr2[0].length; j++) {
      let elem = 0;
      for (let k = 0; k < arr2.length; k++) {
        // arr1[0].length도 가능.
        elem += arr1[i][k] * arr2[k][j];
      }
      result.push(elem);
    }
    newArr.push(result);
  }
  return newArr;
}
```

- 행렬 곱셈을 구현했다.
- for loop를 3번 이상 돌리지 않게 하는 방법에 대해서 고민했지만 필수적이라고 생각이 들었다
- 가장 기본적인 구조 구현
