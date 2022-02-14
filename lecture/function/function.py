"""
함수를 왜 쓸까?
1. 입력대비 항상 다른 아웃풋을 얻기 위해
2. 반복을 없애기 위해
3. 더 직관적으로 코드를 작성하기 위해 -> 한방에 딱 알아볼 수 있게

def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장1>
    ...

"""
from binhex import REASONABLY_LARGE
import rlcompleter


def add(x, y): #매개변수 parameter
    result = x + y
    return result
# 이 함수의 이름은 add이고 입력으로 2개의 x,y 값을 받으며,
#결괏값은 2개의 입력값을 더한 값이다.

x=3
y=4
c=add(x,y) #argument 인자
print(c)

#매개변수(입력값) -> 함수 -> 출력값

#camel 표기법. dannyKim
#매개변수 즉 입력값이 없는 함수
def dannySam():
    return "네"

answer = dannySam() #datatype = string

print(dannySam())


#return 값 즉 결괏값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

"""
빨래하는 기계
1. 물이 나와야 함 -> 함수 (시작버튼)
2. 돌아가야 함 -> 함수(시작버튼 눌르면)
3. 세제도 자동으로 넣어줘야함 -> 함수(시작버튼 누르면)
"""

def waterFlush(start):
    water = 1
    if start == True:
        water = 1
        return water
    else:
        water = 0
        return water

def spin(start):
    roll = 1
    if start == True:
        roll = 1
        return roll
    else:
        roll = 0
        return roll

def soap(start):
    soapStart = 1
    if start == True:
        soapStart = 1
        return soapStart
    else:
        soapStart = 0
        return soapStart