#hash // dictionary(=dict)  {key:value}

# {"apple": "a fruit with red and green colors",
# "banana" : "a fruit with yellow color",
# "cat" = "an alien"}

dic = {'Apple':'A fruit with red and green colors', 'Banana' : 'a fruit with yellow color', 'Cat':'an alien'}

#dictionary 호출
print(dic['Apple'])

dic['Apple'] = "A fruit with white color"
print(dic['Apple'])

#dictionary key and value 추가하기
dic['dog'] = "a cute animal"
print(dic)

dic['human'] = "2009014@2009014 Git"
print(dic)

dic['Banana'] = "A fruit with red color"
print(dic['Banana'])


a= {1: 'a'} #dictionary 생성
print(a)

b = dict()
print(b)


#indexing 아님, dictionart에 값 집어넣기
a[2] = 'b'
a[3] = 'c'
a[6] = 'f'
a[7] = [1,2,3,4]
print(a)

del a[1]
del a[7]
print(a)

#관련된 함수들
#key list 만들기
print(dic.keys())
print(list(dic.keys())) #완전히 리스트로 바꾸기

#key 나열해보기
for key in dic.keys():
    print(key)

#value list 만들기
print(list(dic.values()))

#전부 얻기
print(list(dic.items()))
#여기서 list 지우면 걍 tuple 형태로 나옴

# #전부 지우기
# dic.clear()
# print(dic)

#key를 통해서 value 얻기
print(dic.get('Apple'))
print(dic.get('Banana'))
print(dic.get('humans'))

#우리가 찾고자 하는 key 딕셔너리에 있는지 확인하고 싶을떄
print('human' in dic)