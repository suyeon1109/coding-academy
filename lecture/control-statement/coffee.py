# """
# coffee = coffee - 1 -> coffee -= 1
# coffee = coffee + 1 -> coffee += 1
# """

# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요"))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

#while 문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)


"""
while 문을 사용하여 다음과 같이 별을 표시하는 프로그램을 작성하자.

*
*
*
*
*

"""

star = 1
while star >= 1:
    print("*")
    star += 1
    if star == 5:
        print("*")
        break

star = 1
while star == 1:
    print("*")
    star += 1
    if star == 2:
        print("**")
        star += 1
    if star == 3:
        print("***")
        star += 1
    if star == 4:
        print("****")
        star += 1
    if star == 5:
        print("*****")
        break

count = 0
while count < 5:
    count += 1
    print("*" * count)