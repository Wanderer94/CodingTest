```py
def solution(bandage, health, attacks):
    answer = 0
    time = attacks[-1][0]
    attacks = dict(attacks)
    maintain_time = 0
    current_health = health
    # 공격 시전
    for t in range(1, time + 1):
        # 공격성공시 체력 감소
        if t in attacks:
            current_health -= attacks[t]
            maintain_time = 0
            # 체력이 0 이하가 되었을 경우 사망 처리하고 이후의 공격을 계산하지 않음
            if current_health <= 0:
                current_health = -1
                break
        # 체력 회복
        else:
            maintain_time += 1
            # 추가회복량 성공
            if maintain_time == bandage[0]:
                current_health += bandage[1]
                current_health += bandage[2]
                maintain_time = 0
            else:
                current_health += bandage[1]
            # 최대체력일 경우 체력 유지
            if current_health > health:
                current_health = health
    answer = current_health
    return answer
```

- 파이썬 치고 굉장히 구현이 길었던 문제.
- 고칠 수 있는 부분은 중간에 for문과 계산하는 부분을 함수로 빼서 break를 걸지 말고 return으로 구현했다면 좀 더 간단해 지지 않았을 까
