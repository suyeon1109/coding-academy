#list=array (=열). 파이썬에서만 리스트라고 함
odd = [1, 3, 5, 7, 9] 
#리스트이름 = [element 1, element 2, ...]

#여러가지 리스트의 생김새
a = []  #빈 리스트 empty list
print(a)

b= [1, 2, 3] #정수를 포함한 리스트
print(b)

c = ["Life","is", "too", "short"] #string 을 포함한 리스트
d = [1, 2, "Life", "is"] #string & integer 포함한 리스트
e = [["Life","is", "too", "short"], 1, 2] #integer, list 를 포함한 리스트
f = [1, 2, [3, 4, [5, 6, [7]]]]

#리스트의 인덱싱
print(b[1]) #-> 2
print(b[-1]) #-> 3
print(e[0]) #-> ["Life","is", "too", "short"]

print(b[0] + b[2])
print(e[0][0])
#print(e[2][-1])
print(f[2][2][0])  #3d
print(f[2][2][2][0])  #4d 여기까지 올 일 극히 드믈디

#list 의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[1:4]) # 2, 3, 4

b = a[1:4]
print(b)
print(a[:3]) #[요건 그자리:요건 그 전자리]

#중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
#[3, ['a', 'b', 'c'], 4]
print(a[2:5])
print(a[3][:2])

#리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) #[1, 2, 3, 4, 5, 6]

#리스트 반복
a = [1, 2, 3]
print(a*5)

#리스트 길이 구하기
a = [1, 2, 3, 4, 5, 6, 7, 7, 8]
print(len(a))

# a = [1, 2, 3] #list
# b = "4, 5, 6"
#print(a+b) #절대안됨

a[3] = 7 #값 수정 ㄱㄴ, 한번에 하나밖에 안됨
print(a)

#del 함수로 리스트 element 삭제
del a[3]
print(a)

#리스트 관련 함수들 ⭐️⭐️

#리스트에 element 추가 (append)
a = [1, 2, 3, 4]  #append의 특징상 항상 맨 뒤에 추가
a.append(5)
print(a)

a.append([5,6])
print(a)

#정렬 sort -> 효율성
a = [1, 4, 3, 2, 7, 5]
a.sort()
print(a)

#리스트 뒤집기 reverse
a = [6,5,4,3,2,1]
a.reverse()
print(a)

#위치 반환 index
a = [6,5,4,3,2,1,"a"]
print(a.index(6)) #6이라는 숫자를 가진 element는 몇번째에 있냐?
location = a.index("a") #목적: 스트링 지우기
del a[location]
print(a)

a = ["a", "b", 1, 2, 3, ["c", "d", "e"]]
print(a[5].index("d"))
#string, integer 같이 sort 절대 안됨

#리스트에 element insert
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.append("abc")

#리스트 요소 제거 remove
a = [1,2,3,1,2,3]
a.remove(3) #첫번째꺼만 지움
print(a)

#리스트에서 요소 끄집어내기 pop
a = [1,2,3]
print(a.pop(1)) #index
print(a) #pop 한거만 빼고 나머지만 프린트됨

#리스트에 포함된 element 개수 세기 count
a =[1,2,3,4,5,6,1,2,1,1]
print(a.count(1))


#1. 홍길동씨의 주민번호는 961105-1234567이다. 홍길동씨의
#주민등록번호를 연월일 부분과 그 뒤의 숫자 부분으로 나타내라
#slicing 사용

a = "961105-1234567"
print(a[:5])
print(a[7:])

#2. [1,2,5,4,3] 리스트를

a = [1,2,5,4,3]
a.sort()
a.reverse()
print(a)

#3. 홍길동씨의 과목별 점수는 다음과 같음. 평균?
#국어: 80 수학: 55 영어: 75

a = 80
b = 55
c = 75

print((a+b+c)/3)

#4
#["Life","is", "too", "short"] 리스트를 life is too short 문자열 string로 만들어서 출력하기.

a = ["Life","is", "too", "short"]
# a = str(a)  #["Life","is", "too", "short"]
# print(a)
# a = a.replace("''","")
# a = a.replace(","," ")
# a = a.replace("[","")
# a = a.replace("]"","")

a = ["Life","is", "too", "short"]
print(a[0], a[1], a[2], a[3])
