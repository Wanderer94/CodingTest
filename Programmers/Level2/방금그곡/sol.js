function solution(m, musicinfos) {
  var answer = "";
  const melodys = [
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
    "A",
    "A#",
    "B",
  ];
  let melodyMap = {};
  // 슈도로 짜더라도 순서대로 작성할 것
  // 1. 파싱 및 계산
  let tempmelody = "";
  const parsedMusicinfos = musicinfos.map((musicinfo) => {
    // 1차 파싱
    let [start, end, title, melody] = musicinfo.split(",");
    // 2차 파싱
    // 시간 계산 + 정수 변환
    let [start_time, start_minit] = start.split(":");
    let [end_time, end_minit] = end.split(":");
    let playTime = (+end_time - +start_time) * 60 + (+end_minit - +start_minit);
    if (playTime > melody.length) {
      let repeatCount = Math.floor(playTime / melody.length);
      tempmelody = melody.repeat(repeatCount).slice(0, playTime);
      tempmelody += melody.slice(0, playTime % melody.length);
    } else {
      tempmelody = melody.slice(0, playTime);
      console.log(tempmelody);
    }
    // melody파싱
    if (tempmelody.includes(melody)) {
      let regex = /[A-G]#/g;
      tempmelody = tempmelody.replaceAll(regex, (match) => match[0]);
      if (!answer || answer[1] < playTime) {
        answer = [title, playTime];
      }
      console.log(tempmelody);
      if (!melodyMap.has(title)) {
        melodyMap.set(title, tempmelody.length);
      } else {
        let currentLength = melodyMap.get(title);
        if (currentLength < tempmelody.length) {
          melodyMap.set(title, tempmelody.length);
        }
      }
    }
  });
  return answer;
}
