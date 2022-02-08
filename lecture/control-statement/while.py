"""
while 문의 기본 구조

while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3

조건문이 참인 경우에 indentation 된 수행문장들을 행하라
"""

#열번 찍어 안남어가는 나무 없다
treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d 번 찍었습니다" % treehit)
    if treehit == 10:
        print("나무가 넘어 갔습니다.")
#여기서 if 쓰면 10번 못찍고 한번만 찍고 넘어감
#나무를 10번 찍을때까지 반복해라

prompt = """
1. Add
2. Del
3. List
4. Quit
...
Enter number:"""

number = 0

#number가 4가 될때까지 아래 문장들을 반복해라!!
#4가 되면 이 while 문을 탈출하낟, 끈다
while number != 4:
    print(prompt)
    number = int(input())

#밥을 세번 먹었다면 굶어라 아니면 밥을 세 끼를 무조건 먹어라
meal = 0
while meal < 3:
    print("무조건 먹어")
    meal = meal + 1
    if meal == 3:
        print("굶어라")

#1부러 100까지 더하시오
count = 0
tot = 0
while count < 100:
    tot = tot + count
    count = count + 1
    if count == 100:
        print(tot)


#while 문을ㄹ 사용해서 1~1000까지의 자연수 중 3의 배수의 합을 구하여라
count = 3
tot = 0
while count >= 1 and count <= 1000:
    if count % 3 ==0:
        tot = tot + count
    count = count + 1
print(tot)

# status = ""
# while True: #무한반복
#     if status == "Error":
#         break

# while True:
#     print(1)

#커피머신 기계 만들기.
coffee = 10
money = 300
while money == 300:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break #while 문을 나가라