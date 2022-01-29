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

