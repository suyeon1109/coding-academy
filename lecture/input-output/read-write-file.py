# file = open("/Users/kis/Documents/GitHub/coding-academy/lecture/function/함수.txt", 'w') #w means write
# file.close()

file = open("새파일.txt", 'w')

for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    file.write(data)
file.close()

"""
파일 열기 모드

r = 읽기모드 - 파일을 읽기만 할 때
w = 쓰기모드 - 파일에 내용을 작성할 때 사용
a = 추가모드 - 파일의 마지막줄에 새로운 내용을 추가할 때 사용
"""