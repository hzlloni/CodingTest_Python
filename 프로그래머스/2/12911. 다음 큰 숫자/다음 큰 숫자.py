"""
- int(): 10진수로 변환해 주는 함수
- bin(): 2진수로 변환해 주는 함수
    - bin(n)[2:] : 슬라이싱을 사용하여 진법표시 삭제
- oct(): 8진수로 변환해 주는 함수
- hex(): 16진수로 변환해 주는 함수

"""

def solution(n):
    answer = n + 1
    
    while 1:
        if bin(n)[2:].count('1') == bin(answer)[2:].count('1'):
            return answer
        answer += 1
        

    
