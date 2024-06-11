def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_i = ["code", "date", "maximum", "remain"].index(ext)
    sort_i = ["code", "date", "maximum", "remain"].index(sort_by)
    for d in data:
        # ext 조건이 성립하면 append
        if d[ext_i] < val_ext:
            answer.append(d)
    # sort_by에 해당하는 값을 기준으로 오름차순 정렬
    answer.sort(key=lambda x:x[sort_i])
    return answer