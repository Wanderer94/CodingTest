function solution(files) {
    // var answer = [];
    // let temp = {}
    // for (let i = 0; i < files.length; i++){
    //     const [head, number, tail] = files[i].split(/(\d+)/)
    //     answer.push({head:head, number:number,tail:tail})
    // }
     let answer = files.map(file => {
        const [head, number, tail] = file.match(/^([^\d]+)(\d{1,5})(.*)$/).slice(1);
        return { head, number, tail };
    });
    answer.sort((a,b) => a.head.toLowerCase().localeCompare(b.head.toLowerCase()) || Number(a.number) - Number(b.number))
    
    for (let i = 0; i < answer.length; i++){
        answer[i] =  answer[i].head +  answer[i].number +  answer[i].tail
     }
    console.log(answer)
    return answer;
}