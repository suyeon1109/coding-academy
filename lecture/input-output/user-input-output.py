"""
야 수연아 오늘 5시에 수업이다. -> 입력

"[전송]" -> 함수

출력 = "00:00:00초 김영호님의 메세지: "야 수연아 오늘 5시에 수업이다.""
"""


#사용자의 입력
# a = input() #built-in functions // input(함수의 가장 기본적인 타입은 스트링)
# #무조건 integer 여야 한다면 int(input())
# #리스트여야 한다면 list(input())

# print("당신이 입력한 문자는:", a, "입니다.")

# number = int(input("숫자를 입력하세요: "))
# #숫자 입력하는 순간 넘버에 그 숫자 저장
# print(type(number), number)

#사용자 출력
#1. ㄱ큰 따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too" "short")
print("life"+"is"+"too"+"short") #둘이 같은거임

#2. 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too", "short")

#3. 한 줄에 결과값 모두 출력하기
for i in range(1,101):
    print(i, end = ",") #값 사이사이 이어주는 것

