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

"""
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.
"""

#특정 아이디가 신고당한 횟수를 노가다 하지 않고 계산하는 방법..?
#한번에 한 명의 유저만 신고하게 하기: if len(a)>6 : pass
#"동일한 유저에 대한 신고 횟수는 1회로 처리됩니다. k번 이상 신고된 유저는 게시판 이용이 정지되며" 이해가 안됨
#

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = 0
# k =2

# def solution(id_list, report, k):
#     for i in range(0,):
#         a = input()
#         report = report + 1
#         if str(a) in id_list:
#             print("%d는 신고당했습니다." %str(a))
#         if report == 2 and str(a)
#         else:
#             pass
#     answer = []
#     return answer

"""
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
"""

# indexing/ slicing, int(), 부등호 사용해서 if ~~~만들기
# : 이후로 나오는 문장? 은 //, indexing/ slicing, int() 또 써서 print(~~) 만들기

def solution(array, commands):
    answer = []
    return answer