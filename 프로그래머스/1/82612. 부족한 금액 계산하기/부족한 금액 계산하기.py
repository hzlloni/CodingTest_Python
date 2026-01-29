def solution(price, money, count):
    answer = 0
    for i in range(count):
        new_price = price * (i+1)
        answer += new_price
    
    if(money < answer):
        return answer - money
    else:
        return 0