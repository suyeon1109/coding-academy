f = open("/Users/kis/Documents/GitHub/coding-academy/dailywork/text.txt", "w")

# lines = f.read()  
# for line in lines:
#     line = " "
#     print(line)
# for i in range(0,):
#     data = """Life is too short
#     You need python"""
#     f.write(data)
# f.close()

lines = f.read()  
for i in range(0,):
    data = """Life is too short
    You need Java"""
    print(data.replace("Java", "python"))
f.close()