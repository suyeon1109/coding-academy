# arr =  [1, 1, 3, 3, 0, 1, 1]

# def solution(arr):
#     for i in range(1, len(arr)-1):
#         try:
#             if arr[i-1] == arr[i]:
#                 arr.pop(i)
#             else:
#                 pass
#         except:
#             pass
#     return arr

# print(solution(arr))

"""
1. arr 길이의 숫자만큼 arr[i] == arr[i-1] 인지 확인
2. arr[i] == arr[i-1]면 하나 지우기
3. return


같은 숫자는 싫어
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
입출력 예
arr	                answer
[1,1,3,3,0,1,1]	    [1,3,0,1]
[4,4,4,3,3]	        [4,3]
"""


def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))


"""
가운데 글자 가져오기
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	        return
"abcde"	    "c"
"qwer"	    "we"
"""


def solution(s):
    list(s)
    if len(s) % 2 ==0:
        answer = s[len(s) // 2 - 1] + s[len(s) // 2]
    if len(s) % 2 != 0:
        answer = s[len(s) // 2]
    return answer