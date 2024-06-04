const getPrefix = (strs) => {
  //맨 처음 단어 첫 글자 있는지 없으면 stop
  const prefix = "";
  let check1 = false;
  for (let i = 1; i < strs[0].length; i++) {
    for (let j = 1; j < strs.lenth; j++) {
      if (strs[0].substr(0, i) == strs[j].substr(0, i)) {
        check1 = true;
      } else {
        check1 = false;
      }
    }
    if (check1) {
      prefix = strs[0].substr(0, i);
    } else {
      break;
    }
  }
  return prefix;
};
strs = ["start", "stair", "step"];
console.log(getPrefix(strs));
