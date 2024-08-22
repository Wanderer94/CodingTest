def solution(players, callings):
    name_to_idx = {name: i for i, name in enumerate(players)}

    for call in callings:
        idx = name_to_idx[call]
        # 추월 적용
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        name_to_idx[players[idx]] = idx
        name_to_idx[players[idx - 1]] = idx - 1

    return players
