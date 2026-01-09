def solution(num_list):
    answer = 0
    mul = 1
    list_sum = (sum(num_list))**2
    
    for i in num_list:
        mul *= i
    
    if mul < list_sum:
        return 1
    else:
        return 0