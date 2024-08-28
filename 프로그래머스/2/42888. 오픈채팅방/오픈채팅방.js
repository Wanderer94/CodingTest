function solution(record) {
    var answer = [];
    let result = []
    let record_set = {}
    for (let i = 0; i < record.length; i++){
        const [command, uid, nickname] = record[i].split(" ")
        let recent_nick = ''
        if (command == "Enter"){
            record_set[uid] = nickname
            answer.push({command : command, uid : uid})
        }else if(command == "Change"){
            record_set[uid] = nickname
        }else if(command == "Leave"){
            answer.push({command : command, uid : uid})
        }
    }
    for (let i = 0; i < answer.length; i++){
        if(answer[i].command == "Enter"){
            result.push(record_set[answer[i].uid] + "님이 들어왔습니다.")
        }else if(answer[i].command == "Leave"){
            result.push(record_set[answer[i].uid] + "님이 나갔습니다.")
        }
    }
    return result;
}