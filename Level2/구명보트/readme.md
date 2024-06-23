```py
 def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        if len(people) == 1 or people[0] + people[-1] > limit:
            answer += 1
            people.pop(-1)
        else:
            answer += 1
            people.pop(0)
            people.pop(-1)
    return answer
```

- 하지만 시간 제한에 걸렸다.
- 따라서 left와 right를 사용하는 아이디어로 변경했다.

```py
 def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] > limit:
            right -= 1
        else:
            left += 1
            right -= 1
        answer += 1
    return answer
```

- 해석해 보면 , left와 right를 사용하여, left가 right보다 작거나 같을 때까지 반복한다.
- people[left] + people[right] > limit이라면 right를 줄인다.
- 그렇지 않다면 left를 늘리고 right를 줄인다.
- answer는 while문이 끝날 때마다 +1이 되므로, while문이 끝나면 answer의 값을 return한다.
