'''
0 = false
1 = true
Trrue = true
False= False

1. dictionary a에서 'B'에 해당되는 값을 추출하라
a= {'A':90, 'B':80, 'c':70}

2. a list에서 중복 숫자를 제거하라.
a = [1,1,1,2,2,3,3,3,4,4,5]
'''

a = {'A':90, 'B':80, 'c':70}
print(a['A'])

a = [1,1,1,2,2,3,3,3,4,4,5]
a = set(a)
print(a)