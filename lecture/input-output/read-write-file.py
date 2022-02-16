# file = open("/Users/kis/Documents/GitHub/coding-academy/lecture/function/함수.txt", 'w') #w means write
# # file.close()

# file = open("새파일.txt", 'w')

# for i in range(1,11):
#     data = "%d번째 줄입니다. \n" % i
#     file.write(data)
# file.close()

"""
파일 열기 모드

r = 읽기모드 - 파일을 읽기만 할 때
w = 쓰기모드 - 파일에 내용을 작성할 때 사용
a = 추가모드 - 파일의 마지막줄에 새로운 내용을 추가할 때 사용 update
"""

# f = open("/Users/kis/Documents/GitHub/coding-academy/lecture/input-output/매출액.txt", "r")
# # print(f)

# lines = f.readlines()  #전체 뽑아내기는 lines = f.read()
# for line in lines:
#     line = line.strip() #줄 끝에 있는 줄 바꿈 문자(\n)를 없애줌
#     print(line)
# f.close()

f = open("/Users/kis/Documents/GitHub/coding-academy/lecture/input-output/새파일.txt", "a")
#w는 쓸때마다 모두 초기화됨
#추가하고 싶을땐 a 하면 됨

# data = "\n11번째 줄입니다"
# f.write(data)
# f.close()

"""
11번째 12 번째 ~~~20번ㅐ까지 for loop 사용해서 만들기
"""

for i in range(11,21):
     data = "%d번째 줄입니다. \n" % i
     f.write(data)
f.close() #이거 안하면 무조건 망함

with open("/Users/kis/Documents/GitHub/coding-academy/lecture/input-output/새파일.txt", "a") as f:
    data = "\n11번째 줄입니다"
    f.write(data)  
#32~34번째 줄 코드랑 똑같은거임