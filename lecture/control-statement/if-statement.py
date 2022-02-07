'''
why if statement?

"돈이 있으면 택시를 타고, 돈이 없으면 걸어간다."

"if you have money, take taxi, if not walk."

'''

from sre_constants import FAILURE


money = True #돈을 가지고 있음을 표현
if money:
    print("택시를 타고 가라")
else: #돈 없다는 뜻
    print("걸어 가라")

'''
수학 100점 나오면 컴퓨터 사주고, 100점이 안나오면 혼날거야
'''
math100 = True

if math100:
    print("컴퓨터 사줌")
else: 
    print("혼남")

"""
if 문의 기본 구조

if 조건문:
    수행할 문장 1
    수행할 문장 2
    ...
else:
    수행할 문장 A
    수행할 문장 B

들여쓰기
:콜론 뒤에는 들여쓰기 한 애들만 시행하라는 뜻
"""

#비교연산자 comparison
"""
x < y
x > y
x >= y
x <= y
x == y : 같다
x != y : 같지 않다
"""

x = 2
y = 3
print( x > y)

"만약 3000원보다 많이 있으면 택시를 타고 가고, 아니면 걸어가라"
money = 3000

if money > 3000:
    print("TAXI")
else: 
    print("walk")

"""
다른 연산자들
or
and
not

x or y : x, y 둘 중 하나만 참이어도 참이다
x and y: 둘다 참이어야 참이다
not x: x가 거짓이면 참이다
"""

#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고 그렇지 않으면 걸어가라."

money = 3000
card = True

if money > 3000 or card == True:
    print("택시를 타고 가")
else:
    print("걸어가")

"""
1 in [1,2,4] -> "1이 [1,2,3] 에 있나요?" -> is 1 in [1,2,3] -> true
1 not in [1,2,4] -> "1이 [1,2,3] 에 없나요?" -> is 1 in [1,2,3] -> false

'a' in ['a','b','c'] -> true
'a' not in ['a','b','c'] -> false
"""

#만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타")
else:
    print("걸어가")

#주머니에 돈이 있으면 가만히 있고, 돈이 없으면 카드를 꺼내라
pocket = ['money', 'paper', 'cellphone']

if 'money' in pocket:
    pass
else: print("카드를 꺼내라")

#주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 지하철을 타고,
#돈도 없고 카드도 없으면 걸어가라

# pocket1 = ['money', 'card']
# pocket2 = ['card']
# pocket3 = []

# if 'money' in pocket1:
#     print("taxi")
# if 'card' in pocket2:
#     print("subway")
# if 'money' and 'card' not in pocket3:
#     print("walk")

pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket:
    print("taxi")
else:
    if 'card' in pocket:
        print("subway")
    else:
        print("walk")

pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket:
    print("taxi")
elif 'card' in pocket:
    print("metro")
else:
    print("walk")

#책상위에 연필이 있으면 공부하고, 연필은 없지만 지우개가 있으면 잠을 자고,
#연필은 있지만 노트북이 없으면 공부하고, 셋 다 없으면 게임해라

desk = ['pencil']

if 'pencil' in desk:
    print("study")
elif 'eraser' in desk:
    print("sleep")
else:
    print("game")

#조건부 표현식
score = 60
if score >= 60:
    message = "success"
else: 
    message = "failure" #변수 저장

print(message)

message = "success" if score >= 60 else "failure"
print(message)
