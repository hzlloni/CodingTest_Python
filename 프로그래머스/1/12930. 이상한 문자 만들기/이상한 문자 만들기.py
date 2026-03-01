# 문자열 인덱스 찾는법 : s.find('o') -> "현재 위치”가 아닌 “처음 나온 위치”를 알려줌 -> 사용 불가

# 문자열 인덱스로 접근하기
# >>> hello = 'Hello, world!' 
# >>> hello[0]    # 첫 번째(인덱스 0) 문자 출력
# 'H'

def solution(s):
    answer = ''
    word = s.split(" ")
    
    for i in word:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()

            else:
                answer += i[j].lower()
        answer += " "

    return answer[:-1]