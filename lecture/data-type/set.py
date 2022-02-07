#집합의 특징
# 문자열이랑 비슷
# 중복 안되고 순서 없음 (unordered)

""""
list = [1,1,1,1,1,1,,1,2,3,4,5]
[1,2,3,4,5] -> duplicate 없애고 싶어
.set(list)
"""

s1 = set([1,2,3])
l1 = list(s1)
print(s1)

#index,slicing은 정수빼고 다 똑같음

t1 = tuple(s1)
print(t1[0])

#교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([1,2,3,4,5,6])

#교집합(=intersection) -> &
print(s1 & s2)
print(s1.intersection(s2))

#합집합 -> |(=or)
print(s1 | s2)
print(s1.union(s2))

#차집합 -> -
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

#집합과 관련된 함수들
#값을 추가하는 add
s1 = set([1,2,3])
s1.add(4)
print(s1)

#값 여러개 추가하기
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

#특정값 제거하기 remove
s1 = set([1,2,3])
s1.remove(3) #element 값을 넣어야됨