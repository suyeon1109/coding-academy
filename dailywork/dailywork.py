f = open("/Users/kis/Documents/GitHub/coding-academy/dailywork/text.txt", "w")

# lines = f.read()  
# for line in lines:
#     line = " "
#     print(line)
# for i in range(0,):
#     data = """Life is too short
#     You need python"""
#     f.write(data)
# f.close()

# lines = f.readline()  
# for i in range(0,): 반복할때만 써
data = """Life is too short\nYou need Python"""
f.write(data)
f.close()


"""
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.

단, -10,000 ≤ A, B ≤ 10,000
"""

import random 
A = random.randit(-10000,)   # -10,000 ~ 무한대 까지 범위를 어떻게 설정하는지 기억이 안나서 구글에 쳐봤는데 안나와요!
B = random.randit(10000)    #구글에서 보고 따라했는데 AttributeError: module 'random' has no attribute 'randit' 라고 뜸

if A > B:
    print(">")
if A < B:
    print("<")
if A == B:
    print("==")


"""
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
하지만, 2000년은 400의 배수이기 때문에 윤년이다.

첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
"""

for i in range(0,4000):
    if i % 4 == 0:
        print(1)
    else:
        print(0)