def solution(num):
    count = 0 

    while True:
        if num == 1:
            break
        if num % 2 == 0:
            num = num /  2
            count += 1
        elif num % 2 != 0:
            num = num * 3 + 1
            count += 1
        if count >= 500 and num != 1:
            return -1
        
    return count