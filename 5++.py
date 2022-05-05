#1
string = input("문자를 입력하시오: ")

if ord(string)>= 65 and ord(string)<= 90:
    print("True")
else:
    print("False")

#2
string=input("문자를 입력하시오. : ")

if ord(string)>= 65 and ord(string)<= 90:
    print(string+"는 대문자입니다.")
elif ord(string)>= 97 and ord(string)<= 122:
    print(string+"는 소문자입니다.")
else:
    print("잘못된 값을 입력하셨습니다.")

"""
if string >='A' abd string <='Z':
    print(string+"는 대문자입니다.")
elif string>= 'a' and string<= 'z':
    print(string+"는 소문자입니다.")
else:
    print("잘못된 값을 입력하셨습니다.")
"""

#3
string=input("문자/문자를 입력하시오. : ")

if string >='A' and string <='Z' or string>= 'a' and string<= 'z':
    print(string+"의 아스키코드는 "+str(ord(string))+"입니다.")
else:
    print("아스키코드 "+string+"의 문자열은 "+str(chr(int(string)))+"입니다.")


#4
a = input("문자입력: ")

if a >='a' and a<='z':
    print(a+"의 대문자: "+str(chr(ord(a)-32)))


#5
elif a >='A' and a<='Z':
    print(a+"의 소문자: "+str(chr(ord(a)+32)))
else:
    print("잘못된 값을 입력하셨습니다.")

import random
dice = ["가위","바위","보"]
computer = random.choice(dice)

player = input("(가위, 바위, 보) 중에서 하나를 선택하세요: ")
print("사용자:",player,"컴퓨터:",computer)

if player==computer:
    print("비겼음!")
elif player=="가위":
    if computer=="바위":
        print("졌음!")
    if computer=="보":
        print("이겼음!")
elif player=="바위":
    if computer=="가위":
        print("이겼음!")
    if computer=="보":
        print("졌음!")
else:
    if computer=="가위":
        print("졌음!")
    if computer=="바위":
        print("이겼음!")


#4
f = int(input("시작수: "))
s = int(input("끝수: "))
a=1
count1=0
count2=0

"""
for i in range(f,s+1):
    if i %2==1:
        count2+=i
    else:
        count1+=i
print("홀수합 = "+str(count2)+"\n짝수합 = "+str(count1))
"""

while a<= s:
    if a %2==1:
        count2+=a
    else:
        count1+=a
    a+=1
print("홀수합 = "+str(count2)+"\n짝수합 = "+str(count1))



#5
num=int(input("원하는 단: "))
b=1

print(num,"단")

"""
#for i in range(1,10):
#    print("7 *", i, "=", 7*i)


while b<=9:
    print(num,"*", b, "=", num*b)
    b+=1

#5-1

for i in range(1,10):
    print("7 *", a, "=", 7*a)
    a-=1
"""
a=9
while a>=1:
    print("7 *", a, "=", 7*a)
    a-=1



#1
string = input("문자를 입력하시오: ")

if ord(string)>= 65 and ord(string)<= 90:
    print("True")
else:
    print("False")


#2
string=input("문자를 입력하시오. : ")

if ord(string)>= 65 and ord(string)<= 90:
    print(string+"는 대문자입니다.")
elif ord(string)>= 97 and ord(string)<= 122:
    print(string+"는 소문자입니다.")
else:
    print("잘못된 값을 입력하셨습니다.")

"""
if string >='A' abd string <='Z':
    print(string+"는 대문자입니다.")
elif string>= 'a' and string<= 'z':
    print(string+"는 소문자입니다.")
else:
    print("잘못된 값을 입력하셨습니다.")
"""


#3
string=input("문자/문자를 입력하시오. : ")

if string >='A' and string <='Z' or string>= 'a' and string<= 'z':
    print(string+"의 아스키코드는 "+str(ord(string))+"입니다.")
else:
    print("아스키코드 "+string+"의 문자열은 "+str(chr(int(string)))+"입니다.")



#4
a = input("문자입력: ")

if a >='a' and a<='z':
    print(a+"의 대문자: "+str(chr(ord(a)-32)))
#5
elif a >='A' and a<='Z':
    print(a+"의 소문자: "+str(chr(ord(a)+32)))
else:
    print("잘못된 값을 입력하셨습니다.")

