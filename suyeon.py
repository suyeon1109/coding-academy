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