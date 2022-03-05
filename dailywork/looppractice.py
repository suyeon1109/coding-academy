"""
******
11줄
"""

# a = "*" * 6
# for _ in range(0,11):
#     print(a)


"""
for 문을 이용해서 
*****
****
***
**
*
"""

a = "*"
b = 6
for i in range(0,5):
    if b <=6:
        b = b - 1
        print(a * b)
        #희귀답안

# a = "*"
# for i in reversed(range(1,6)):
#     print(a * i) #명품답안

"""
*******
*     *
*     *
*     *
*     *
*******

"""

a = "*"
b = 0
for i in range(0,6):
    if b ==0:
        print(a * 7)
    b = b + 1
    if b >= 1 and b <=4:
        print(a + " " * 5 + a)
    if b==5:
        print(a * 7)

"""
for loop을 통해서 

666666
55555
4444
333
22
1
22
333
4444
55555
만들기
"""

a = 7
b = 0

# for i in range(0,5):
#     a = a-1
#     print(str(a) * a)
#     if a == 2:
#         for a in range(0,5):
#             a = a + 1
#             print(str(a) * a)
            #40점짜리

    # for a in range(0,5):
    #     b = b + 1
    #     print(str(b) * b)

for i in range(0,10):
    if i <5:
        a = a-1
        print(str(a) * a)
    if i >= 5: #else 라고 써도 됨
        b = b + 1
        print(str(b) * b)



    #print(reversed(str(a)* a))

    # sixtoone = str(a) * a
    # c = reversed(sixtoone)
    # print(str(c))


"""
0
01
012
0123
01234
012345
"""

a = "0"
b = 1
c = 0

for i in range(0,8):
    c = c + 1
    d = "1" * c
    b = b + int(d)
    print(str(a)+str(b-1))

#for i in range(6):
#   for j in range(i+1):
#       print(j,end="")
#   print()
#모범답안

"""
1~100까지의 수 중에서 홀수와 홀수의 합을 실행 결과와 같이
출력하는 프로그램을 작성하시오.
(1+3+5+...+99)
"""
a = 0

for i in range(0,100):
    if i % 2 ==1:
        a = a + i
print(a)