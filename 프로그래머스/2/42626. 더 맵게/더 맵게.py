import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # list를 min heap으로 변환
    while scoville[0] < K:
        answer += 1
        new_food = heapq.heappop(scoville) + (2 * heapq.heappop(scoville))
        heapq.heappush(scoville, new_food)
        if len(scoville) == 1 and scoville[0] < K: # 음식을 더 이상 만들 수 없는 경우
            return -1
    return answer
