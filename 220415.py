def solution(array, commands):
    # for i in range(0,len(commands)):
    #     print(commands[i])
    #index 

    for each in commands:
        print(each)
    #element

    
    for i,each in enumerate(commands):
        print(i) # -> 0,1,2,...
        print(each) # -> [1,2,3], [4,4,1], [5,6,7]


    # answer = [] 
    # for x in range(0,len(commands)):
    #     i = commands[x][0]
    #     j = commands[x][1]
    #     k = commands[x][2]
    #     # if len(array[i-1:j]) > k-1:
    #     array2 = array[i-1:j]
    #     array2.sort()
    #     print(array2)
    #     answer.append(array2[k-1])
    # print(answer)
    # return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])