"""
기본 구조

for 벼ㄴ수 in list(/tuple/string):
    수행할 문장 1
    수행할 문장2
    ...
    
"""

#for문도 반복문
test_list = ['one', 'two', 'three']
for i in test_list: #i 는 각각의 element 의미
    print(i)

#1부터 10까지 들어있는 리스트를 전부 출력하시오(for 문을 사용해서)
test_list = [1,2,3,4,5,6,7,8,9,10]
for i in test_list: #i 는 각각의 element 의미
    print(i)

#다양한 for 문의 사용
a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first, last)

for i in a:
    print(i) #(,) 이런것들도 같이 프린트되게 하려면

"""
총 5명의 학생이 시험을 보았는데 셤점수가 60점 넘으면 합격, 미만은 불합격
합격인지 불합격인지 결과를 보여주시오.

1. 총 5명의 학생들의 점수가 달린 리스트가 주어진다
2. 각각의 점수를 확인해 60점이 넘으면 합격
3. 각각의 점수를 확인해 60점 못넘으면 불합격

이런식으로 process를 적어두자
"""

scores = [90, 25, 67, 45, 80]
# for i in scores and i >= 60:
#     print("합격")
#     if i in scores and i < 60:
#         print("불합격")

for i in scores:
    if i >= 60:
        print("합격")
    elif i < 60:
        print("불합격")

"""
총 5명의 학생이 시험을 보았는데 셤점수가 60 가장 빨리 넘긴 학생을 뽑으시오.
"""

scores = [90,25,67,45,80]
for score in scores:  #score 라고 하면 그냥 허용? 도;ㅁ
    if score < 60:
        continue
    print("축하합니다. 당신의 점수는: ", score)

#range
#slicing이라 비슷
a = range(10)
print(a)

a = range(1,11)
print(a)

add = 0
for i in range(1,11): #range 가 (1,11)이면 1~10
    add = add + i
print(add)

scores = [90,25,67,45,80]
for score in range(len(scores)): #range가 5라는 소리 -> score 가 1,2,3,4,5
    if scores[score] < 60: #인덱싱을 한거임
        continue
    print("축하합니다 당신의 점수는:", scores[score])


#구구단 만들기
#2단 루프 2D
#nested for loop
for i in range(2,10): #2단부터 9단
    for j in range(1,10): #2x1~2x9
        print(i, "x", j, ":", i * j)
    print("")

#list comprehension 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
#[3,6,9,12]

#이걸 한줄로 쓸 수 있음. 이거쓰면 ㄹㅇ 고수
a = [1,2,3,4]
result = [num * 3 for num in a]
print(num)

#짝수에다가만 3을 곱하여 result로 출력하라
#append 안에 if 문 쓰면 안됨
a = [1,2,3,4]
result = []
for num in a:
    if num % 2 == 0:
        result.append(num*3)
    else:
        result.append(num)
print(result) #순서 똑같음


#찐 고수 인정하는 코드
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 ==0]
#result = [6,12]

for num in a:
    if num%2==0:
        result.append(num * 3)

#위에 두개 같은거임

"""
[ONE LINED CODE]

[표현식 for 객체 in 반복가능개체 if 조건문]
= [num * 3 for num in a if num % 2 ==0]
"""

#너무 고수여서 잘 안쓰게 됨
result = [x*y for x in range(2,10)
            for y in range(1,10)]
print(result) #구구단처럼 하나하나 매칭. 이렇게는 잘 안씀.


"""
연습문제
1. for 문을 사용해서 1 부터 100까지의 숫자를 출력하시오.

2. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다
[70,60,55,75,95,90,80,80,85,100]
for 문을 사용하여 A 학급의 평균점수를 구해보자

3. list 중에서 홀수에만 2를 곱하여 저장하는 코드가 있다. 이것을
list comprehension 으로 바꿔라.

numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 ==:
        result.append(n*2)
"""

#1
for i in range(1,101):
    print(i)

#2
a = [70,60,55,75,95,90,80,80,85,100]
b = 0

for i in a:
    b = b + i
print(b / len(a))

# while count < 100:
#     tot = tot + count
#     count = count + 1
#     if count == 100:
#         print(tot)

#3
numbers = [1,2,3,4,5]
result = []
# for n in numbers:
#     if n % 2 ==:
#         result.append(n*2)

result = [num * 2 for num in numbers if num % 2 == 1]
print(result)