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