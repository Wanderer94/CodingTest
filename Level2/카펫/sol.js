function solution(brown, yellow) {
  var answer = [];
  let ab = (brown + 4) / 2;
  for (let i = 0; i < ab; i++) {
    let a = i;
    let b = ab - i;
    if (yellow == (a - 2) * (b - 2)) answer = [a, b];
  }
  return answer;
}
