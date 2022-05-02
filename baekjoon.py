"""
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
"""

# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# for i in A:
#     if i < X:
#         print(i)


"""
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고,
각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

출력
첫째 줄에 N의 사이클 길이를 출력한다.
"""

N = input()
if int(N) >=0 and int(N) <= 99:
    while int(N) == newnum:
        for i in range():
            a = N
            newnum = int(a[-1] + a[0])
            a = str(newnum)



def solution(participant, completion):
    for each, index in enumerate(completion):
        if each != participant:
            del participant[index]
    answer1= str(participant[0:len(participant)])
    answer= answer1[2:len(answer1)-2]
    return answer


#1
cm = int(input("변환하려는 센치미터는?"))
print("인치(실수):", cm / 2.54)
print("인치(정수):", int(cm / 2.54))

#2
x = 7
a = 5
b = 3
y = x**2 + (b*x)/a + (b/(2*a))**2
print("y값은:", y)

#3
p = int(input("참석자의 수를 입력하시오:"))
print("치킨의 수:", p)
print("콜라의 수:", p * 2)
print("케익의 수:", p * 4)

#4
print("파이썬은 쉽지만", end= " ")
print("매우 유용한", end= " ")
print("프로그래밍 언어입니다")

#5
money = int(input("##교환할 돈은? "))
c500 = int(money/500)
print("500원짜리 ==>", c500, "개")
rm = money - c500*500

c100 = int(rm/100)
print("100원짜리 ==>", c100, "개")
rm2 = rm - c100*100

c50 = int(rm2/50)
print("50원짜리 ==>", c50, "개")
rm3 = rm2 - c50*50

c10 = int(rm3/10)
print("10원짜리 ==>", c10, "개")
rm4 = rm3 - c10*10

print("바꾸지 못한 잔돈 ==>", rm4, "원")


#6
x = int(input("첫번쨰 수를 입력하세요: "))
y = int(input("두번쨰 수를 입력하세요: "))

print("바꾸기 전---------")
print("첫번쨰 수:", x)
print("두번쨰 수:", y)

x,y = y,x

print("바꾼후---------")
print("첫번쨰 수:", x)
print("두번쨰 수:", y)