# 문자를 숫자로 바꾼 후, 계산하여 다시 문자로 변경해주기
# ord -> chr
# test:     print(chr((ord('a') + 1)))

def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            result = ' '
            answer += result
        elif i.islower():
            result = chr((ord(i) - ord('a') + n)%26+ord('a'))
            answer += result
            
        elif i.isupper():
            result = chr((ord(i) - ord('A') + n)%26+ord('A'))
            answer += result
    
    return answer