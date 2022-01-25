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