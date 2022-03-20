#가장 많이 사용. 필수 툴
# result = 0 

# def add(num):
#     global result #global = 외부에 있는 변수인 result를 쓰겠다
#     result = result + num
#     return result

# print(add(3))
# print(add(4))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result + num
        return self.result


#A유저꺼 계산기
cal1 = Calculator()

#B user
cal2 = Calculator()

#C user
cal3 = Calculator()


#A user
print(cal1.add(4))
print(cal2.add(3))