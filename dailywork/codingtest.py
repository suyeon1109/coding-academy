"""
컴퓨터가 1~100 숫자(정수 범위) 중 하나를 랜덤으로 정합니다. (이를 알려주지 않습니다.)
사용자는 이 숫자를 맞추어야 합니다.
입력한 숫자보다 정답이 크면 → "UP" 출력,
입력한 숫자보다 정답이 작으면 → "DOWN" 출력.
정답을 맞추면 → "정답"을 출력하고, 지금까지 숫자를 입력한 횟수를 알려줍니다.


컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.
이 숫자를 맞춰주세요.
1~100 숫자 입력:50
DOWN
1~100 숫자 입력:25
UP
1~100 숫자 입력:38
DOWN
1~100 숫자 입력:32
UP
1~100 숫자 입력:35
UP
1~100 숫자 입력:37
DOWN
1~100 숫자 입력:36
정답입니다! 7회 만에 맞췄어요.
"""

# import random
# n = random.randint(1,100)

# count = 0

# while True:
#     A = int(input())
#     count = count + 1
#     if A == n:
#         print("정답입니다! %d회 만에 맞췄어요." % count)
#         break
#     elif A > n:
#         print("Down")
#     else:
#         print("UP")

"""
숫자형 배열을 선언한후

for문과 if,else문만 사용해서 제일 큰값,제일 작은값, 중간값을 추출하기

■출력예시:

제일 큰 값은 5 입니다.

제일 작은 값은 1입니다.

중간값은 3입니다.
"""

A = [1, 2, 3,4, 5]
A.sort()
print(A)

a = 0
b = 0

for i in A:
    if i == A[-1]:
        a = i
        print("제일 큰 값은 %d 입니다." % a)
    if i == A[0]:
        b = i
        print("제일 작은 값은 %d 입니다." % b)
    if i == (A[-1] + A[0])/2:
        print("중간값은 %d 입니다." % int((a+b)/2))
    else:
        print("")