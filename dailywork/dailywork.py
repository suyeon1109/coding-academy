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

# import random 
# A = random.randit(-10000,)   # -10,000 ~ 무한대 까지 범위를 어떻게 설정하는지 기억이 안나서 구글에 쳐봤는데 안나와요!
# B = random.randit(10000)    #구글에서 보고 따라했는데 AttributeError: module 'random' has no attribute 'randit' 라고 뜸

# if A > B:
#     print(">")
# if A < B:
#     print("<")
# if A == B:
#     print("==")


"""
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
하지만, 2000년은 400의 배수이기 때문에 윤년이다.

첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
# """
# B = random.randit() #NameError: name 'random' is not defined
# for i in range(0,4000):
#     if i % 4 == 0:
#         print(1)
#     else:
#         print(0)


"""
흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다.
사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다.
"Quadrant n"은 "제n사분면"이라는 뜻이다.

예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다.
점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.

점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다.
(−1000 ≤ y ≤ 1000; y ≠ 0)

출력
점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다
"""

x = int(input())
y = int(input())

for i in range(-1000,1000):
    if x ==0:
        pass
    if y==0:
        pass
    if x > 0 and y >0:
        print("1사분면")
    if x > 0 and y < 0:
        print("4사분면")
    if x < 0 and y >0:
        print("2사분면")
    if x < 0 and y < 0:
        print("3사분면")

#~사분면 하나씩만 나오게 하려면 어떻게 하는지?!