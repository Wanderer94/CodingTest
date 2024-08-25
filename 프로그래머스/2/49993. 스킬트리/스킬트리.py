def solution(skill, skill_trees):
    answer = 0
    stack = ''
    for skill_tree in skill_trees:
        for s in skill_tree:
            if s in skill:
                stack += s
        if skill[:len(stack)] == stack:
            answer += 1
        stack = ''
    return answer

