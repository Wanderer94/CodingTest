def solution(nums):
    answer = 0
    N = len(nums)
    ans = []
    for i in nums:
        if i not in ans and len(ans) < N/2:
            ans.append(i)
        if len(ans) == N/2 or i == nums[-1]:
            ans = set(ans)
            ans = list(ans)
            answer = len(ans)

    return answer
