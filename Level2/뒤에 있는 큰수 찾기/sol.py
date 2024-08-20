def solution(numbers):
    answer = []
    num_len = len(numbers)
    for i in range(num_len):
        number = numbers[i]
        for j in range(i,num_len):
            if number < numbers[j]:
                answer.append(numbers[j])
                break
            elif j == num_len - 1:
                answer.append(-1)
    return answer