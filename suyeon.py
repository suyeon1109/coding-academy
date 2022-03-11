print("I love NCT")
print("I love MonstaX")

print("-------------------------")

num = 10
while num>0:
    print(num)
    print("above0")
    num = num - 1
print(num)
print("finally zero")

print("-------------------------")

a = 1
b = 1
while a<10:
    b = 1
    while b<10:
        print(a*b)
        b = b+1
        print("idnyl")
    a = a+1
    print("complete")
print("Full Table")


#main() : 우리가 일반적으로 작성하는 코드 영역은 main() 안에 있는 영역
#우리가 프로그램 실행할때 컴퓨터는 main() 안에 있는 것부터 읽는다
#main() 의 영역: 파이썬에서 들여쓰기가 없는 영역 (def 빼고)
#프로그램이 실행된다 == 컴퓨터가 그 구간을 읽는다

def func1():
    print("This is a func1")
    func2()
def func2():
    print("This is a func2")
    func1()

#==순환참조 , 왠만하면 하지 말자, 메모리 꽉찰때까지 계속 반복

def generalAdd(*args): #tuple: 괄호 안에다가 여러 값들을 넣어놓은 structure
    result=0
    for thing in args:
        result+=thing #result=result+thing
    return result

print(generalAdd(1,2,3,4,5))
print(generalAdd(10,9,8,7,6,5,4,3,2,1))
print(generalAdd(3,3,3,3,3,3))#중복 허용

print("------------------------------")

#infinite loop
#while 1:
    #print("infinite loop")
#while True:
    #print("This never ends") #이거는 안나옴 무슨짓을 해도 왜냐면 위에꺼가 무한대로 나와서

#break-무슨 일이 있던 간에 반복문 탈출
val1=10
while val1>0:
    print(val1)
    if val1==3:
        break
    val1-=1
print("outside the loop")
print(val1)

print("---------------------------")


#continue - 조건 확인 절차로 다시 넘어감
limit=100
totalsum=0
while limit>0:
    if limit%3==0:   #%는 나머지
        totalsum+=limit
        limit-=1
    else:
        limit-=1
        continue
print(totalsum)  #100이하의 3의 배수의 총합을 구하는 것
print("---------------------------")


'''501부터 1000까지 2와 5의 배수의 합을 구하기
result: 225250'''

limit=1000
totalsum=0
while 501<=limit<=1000:
    if limit%2==0:   #%는 나머지
        totalsum+=limit
        limit-=1
    else:
        limit-=1
        continue

limit=1000
totaladdition=0
while 501<=limit<=1000:
    if limit%5==0:   #%는 나머지
        totalsum+=limit
        limit-=1
    else:
        limit-=1
        continue

limit=1000
toTalsum=0
while 501<=limit<=1000:
    if limit%10==0:
        toTalsum+=limit
        limit-=1
    else:
        limit-=1
        continue
    
print(totalsum+totaladdition-toTalsum)

print("---------------------------")
print("jdhnvkdsmdclokfmv")

limit=1000
result=0
while limit>500:
    if limit%2==0:
        result+=limit
    if limit%5==0:
        result+=limit
    if limit%10==0:
        result-=limit
    limit-=1
print(result)
#while 한번만 쓰고 풀기
print("---------------------------")
print("ajsncskdmco")

#for
#for 변수 in range/ for 변수 in 리스트
for i in range(1,11,2):  #range(a,b,c): a부터 b-1까지의 값을 c의 간격으로 반복해주는 함수
    print(i*i)                   #여기서는 1 3 5 7 9

for i in range(1,10):
    for j in range(1,10):    #c가 1일ㄸㅐ는 생략가능
        print(i*j)
        print("LOL")
    print("complete")
print("Full table")
print("---------------------------")

name=["Kim","Lee","Park","Choi","Jeong"]
for k in name:    #k는 name이라는 list안에 있는 각 element들이 들어감
    print((name.index(k)+1)*k)   #index는 그 element 의 index (몇번째인지)를 나타냄


#for
#for 변수 in range/ for 변수 in 리스트
for i in range(1,11,2):  #range(a,b,c): a부터 b-1까지의 값을 c의 간격으로 반복해주는 함수
    print(i*i)                   #여기서는 1 3 5 7 9

for i in range(1,10):
    for j in range(1,10):    #c가 1일ㄸㅐ는 생략가능
        print(i*j)
        print("LOL")
    print("complete")
print("Full table")
print("---------------------------")

name=["Kim","Lee","Park","Choi","Jeong"]
for k in name:    #k는 name이라는 list안에 있는 각 element들이 들어감
    print((name.index(k)+1)*k)   #index는 그 element 의 index (몇번째인지)를 나타냄

"""
일요일:
N값을 입력 받아 1부터 N까지의 수 중에서 소수를 구하는 프로그램을 작성하시오.

소수 : 1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수

월요일:
아래 결과 프린트하기
* 
***
*****
*******
*********
***********
*********
*******
*****
***
*

화요일:
아래 결과 프린트하기
0 1 2 3 
1 2 3 4 
2 3 4 5 
3 4 5 6 

수요일:
월드컵은 4년에 한 번 개최된다. 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

목요일:
리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
"""

#5
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []


for i in range(0,len(low_prices)):  
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)


#4
for i in range(2002,2051):
    if i % 4 == 2:
        print(i)


#3
a = -1
for i in range(0,4):
    a = a+1
    print(str(a), str(a+1), str(a+2), str(a+3))


"""
약수가 2개
"""

# N = int(input())
# for i in range(0,N):
#     if i % 2 == 0:
#         print(i)

#2
a = -1

for i in range(0,13):
    if i <= 6:
        a = a+2
        print("*" * a)
    else:
        a = a-2
        print("*" * a)



# a = "*"
# b = 6
# for i in range(0,5):
#     if b <=6:
#         b = b - 1
#         print(a * b)



# a = "*"
# b = 

# for i in range(0,10):
#     if i <5:
#         a = a+1
#         print(str(a) * a)
#     if i >= 5: #else 라고 써도 됨
#         b = b - 1
#         print(str(b) * b)