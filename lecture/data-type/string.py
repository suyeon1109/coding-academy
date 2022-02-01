#문자열: 단어등으로 구성된 문자들의 집합

a=1234
a="1234"

#문자열에 작은 따옴표 포함시키기
food = "python's favorite food is perl"
print(food)

#문자열에 큰따옴표 포함시키기
say = '"python is very easy" he says.'

#백슬래시 \ 를 사용해서 작은 따옴표와 큰따옴표를 문자열에 포함시키기
food = 'python\s favorite food is perl'
say = "\"python is very easy. \" he says."

#여러 줄인 문자열을 변수에 대입하고 싶을 때
#줄을 바꾸기 위한 escpae code \n 삽입
multiline = "life is too short \n you need python."
print(multiline)

#연속된 작은따옴표 3개를 이용해 multiline 만들기
multiline = '''Life is too short
You need python
'''
print(multiline)

#문자열 더해서 연결하기 (concatenation)
head = "python"
tail = " is fun!"
print(head + tail)

#문자열 곱하기
a= "python "
print(a * 3)

# 문자열 곱하기 응용
print("=" * 50)
print("welcome to suyeon's calculator program")
print("press '5' to start calculator")
print("=" * 50)

#문자열 길이 구하기
a= "welcome to suyeon's calculator program"
print(len(a)) #len=length

#문자열의 indexing과 slicing
#indexing= 뭔가를 가리킨다 apple
#slicing= 뭔가를 잘라낸다

a= "welcome to suyeon's calculator program"
print(a[0]) #indexing
print(a[1])
print(a[-1])
print(a[-2])
print(a[-0])

print(a[0:5]) #slicing
print(a[4:4]) #안나옴

#print(a[:]) #전체 프린트
#print(a[:3]) #3까지

#local = "서울특별시 동작구 신대방제2동"
#si = "local[0:5]"
#gu = "local[6:8]"
#dong = "local[11:]"

#print(si + gu + dong)


#replacement
#특정 문자를 다른걸로 대체
#immutable -> 선언하면 다른 식으로 바꿀 수 없다
local = "서울동시흥동" #->서울시시흥동
#local[2] = "시" #X

print(local[:1])
print(local[:2] + "시 " + local[3:])

new_local = local[:2] + "시 " + local[3:]
print(new_local)

"현재 온도는 18도 입니다."
"현재 온도는 20도 입니다."
"현재 온도는 30도 입니다."


#formatting 문자열의 대입
degree = 20
print("현재 온도는 %d도 입니다." % degree) #d=digit
print("현재 습도는 %d도 입니다." % degree)
print("현재 풍속은 %d도 입니다." % degree)

count = 4
print("저는 %s조각의 피자를 먹었습니다." % count) #s=string

print("오늘의 기온은 %d도이고, 저는 너무 추워서 %s조각의 피자를 먹었습니다." %(degree, count))

"""
%d = integer
%s = string
%f = 소수
%c = 문자
"""

print("error is %d%%" % 98)
#or
number = "98"
print("error is", number+"%") #근데 이건 걍 별로니까 쓰지마

print("%10s" % "hi") #10s=10개짜리 공백열. 쓸일없음

f = 3.42134234
print("%0.4f" % f) #0.4=[0:5]효과

#format 함수 이용한 formatting
print("I eat {0} apples and I love {1} {2}." .format("five", "Danny", "Kim"))
print("I eat {number} apples and I love {firstName} {lastName}." .format(number = "five", firstName = "Danny", lastName = "Kim"))


#왼쪽정렬
print("{0:<50}".format("HI")) #HI 기준으로 내 오른쪽에 50
#가운데정렬
print("{0:^50}".format("HI"))
#오른쪽정렬
print("{0:>10}".format("HI"))

#f 문자열 포매팅
name = "김수연"
age = 18
print(f"나의 이름은 {name} 입니다. 저는 {age}살 입니다. 저는 내년에 {age+1}살이 됩니다.")



#문자 개수 세기 (count)
stringValue = "sdahjbakjdhbvkaaaajhdsbzckjnbdaaaajd aaaaakv"

print("stringValue의 개수는: ", len(stringValue))
print(stringValue.count('a'))

numberOfas = stringValue.count('a')
numberOfbs = stringValue.count('b') #.count = 함수 .=~의

print(numberOfas + numberOfbs)


#문자의 위치 알려주기 find & index(index를 알고시퍼)
print(stringValue.find('z'))
print(stringValue[23])
print(stringValue.index('z')) #이건 답 없으면 걍 꺼져버리니까 걍 find 쓰셈

#문자열 삽입 join
print(",".join('ABCDEF'))

#문자열의 대문자 & 소문자
print(stringValue.upper())

text = "                    안녕하세요, 저는 김영호입니다. 이번 프로젝트의 과제는             "

#왼쪽공백지우기
print(text.lstrip()) #()=input 매개변수

#오른쪽공백지우기
print(text.rstrip())

#양쪽공백지우기
print(text.strip())

#문자열 바꾸기 replace
a = "Life is too short"
print(a.replace("Life is", "You are"))

#문자열 나누기 split
a= "Life is too short"
print(a.split())

b= "a:b:c:d"
print(b.split(":"))

b= "a:b-c-d"
print(b.split(":"))

b= "a:b-c-d"
print(b.split("-"))

