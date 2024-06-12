```py
def solution(players, callings):
    answer = []
    for call in callings:
        player_index = players.index(call)
        # 추월 적용
        players[player_index] = players[player_index - 1]
        players[player_index - 1] = call
    answer = players
    return answer
```

- 위의 코드는 최초 답안이다 하지만 index함수가 O(n)이기 때문에 시간 초과가 발생한다.
- 이를 해결하기 위해 enumerate를 사용하여 index 대신 for문을 통해 값을 확인하고 break로 빠져나온다.

```py
def solution(players, callings):
    answer = []
    for call in callings:
        #index 대신 최소화 하기 위해
        for i, player in enumerate(players):
            # 추월 적용
            if player == call:
                prev_player = players[i - 1]
                players[i], players[i - 1] = prev_player, player
                break
        # player_index = players.index(call)
        # # 추월 적용
        # players[player_index] = players[player_index - 1]
        # players[player_index - 1] = call
    answer = players
    return answer

```

- 하지만 이경우에도 시간초과가 발생한다.
- enumerate를 사용하면 index를 사용하지 않아도 되므로, O(n)이 아닌 O(1)로 줄일 수 있다.
- 이를 위해 dictionary를 사용하여 key:value로 player와 index를 저장하고 call을 value로 찾아서 index를 찾는다.

```py
def solution(players, callings):
    name_to_idx = {name: i for i, name in enumerate(players)}

    for call in callings:
        idx = name_to_idx[call]
        # 추월 적용
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        name_to_idx[players[idx]] = idx
        name_to_idx[players[idx - 1]] = idx - 1

    return players
```

- 이렇게 하면 시간복잡도가 O(n)으로 줄어들었다.
- 더 나은 성능을 위해서는, dictionary를 사용하여 key:value로 player와 index를 저장하고 call을 value로 찾아서 index를 찾는 방법을 사용하는 것이 적합하다는 것을 알 수 있다.
