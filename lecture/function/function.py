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
def dannySam1():
    return "네"

answer = dannySam1() #datatype = string

print(dannySam1())


#return 값 즉 결괏값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

#입력값도 없고 결과값도 없는 함수
def dannySam():
    print("네")

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


#매개변수 저장해놓기
def add(abc,befg):
    return abc+befg

result = add(befg = 300, abc = 128)
result2 = add(abc = 1, befg = 400)
print(result, result2)


def add_many(*args):  #* = all
    print("args:", type(args))
    result = 0
    for i in args:
        result = result + i
    return result

#tuple = list, 요소들이 삭제/수정,생성이 도중에 안된다

result = add_many(1,2,3,4,5,6,7,8,9,10) #tuple향식으로 들어감
result2 = add_many(3,6,9,12)
print(result, result2)

#좀 복잡
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result + i
    return result

#add_mul(choice = "add", args = (1,2,3,4,5,6,7,8,9,10))
add_mul("add", 1,2,3,4,5,6,7,8,9,10)


#주어진 자연수가 홀수인지 짝수인지 판별해주는 함수 is_odd 를 작성해보자
def is_odd(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd"

print(is_odd(999))

#args 원래 잘 안쓰는거
#args 쓰는 이유는 내가 몇개 받을지 몰라서
#args는 랜덤한 튜플이고 매개변수가 아님. 잠깐만 매개변수고

#입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성해보자
#(단 입력으로 들어오는 수의 개수는 안정해짐)
#len 함수 사용할 것

# for i in a:
#     b = b + i
# print(b / len(a))

b = 0 #없어도됨

def average(*args):
    for i in args:
        b = b + i
        return (b / len(args))

#함수의 결과값은 항상 하나다.

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(7,9)
print(result) #결과는 tuple 형식으로 [16,63]

result_add, result_mul = add_and_mul(7,9) #튜플로 값 2개 나오니까 2개로 나눠가지는건 됨
print(result_add)
print(result_mul)

# def say_nick(nick):
#     if nick == "바보":
#         return #여기서 걍 빠져나오는거
#     print("나의 별명은 %s입니다" % nick) #여긴 if에 해당되면 프린트 안됨
# say_nick("야호")
# # say_nick("바보")

#매개변수의 초깃값 미리 설정하기
def say_myself(name = "Danny", old = 20, man=True):
    print("my name is %s" % name)
    print("my age is %d" % old)
    if man:
        print("I am Man")
    else:
        print("I am Woman")

#위에껀 인풋값 따로 설정 안해도 프린트 잘 됨(초깃값 있음)

say_myself("suyeon", 18, False)
say_myself(man = False, name = "suyeon", old = 18)
say_myself(man = False) #초깃값이 있으면 원래꺼 똑같은데 여자로만 바뀐경우

#scope 범위
a = 1
def vartest(a):
    a = a + 1

print(vartest(a)) #2
print(a)          #1

a = 1
def vartest2():
    global a #함수 안에서 외부에 존재하는 변수를 선택
    a = a + 1

vartest2()
print(a)


a = [1,2,3,4,5,6,7,8,9,10]
tot = sum(a) #python 자체에서 만들어준 함수도 쓸 수 있음
print(tot)