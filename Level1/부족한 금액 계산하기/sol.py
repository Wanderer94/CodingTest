def solution(price, money, count):
    answer = -1
    total_price = 0

    total_price = count * (count + 1) / 2 * price

    if total_price-money <= 0:
        answer =0
    else:
        answer = total_price - money


    return answer