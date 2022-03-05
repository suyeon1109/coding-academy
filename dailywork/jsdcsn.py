f = open("/Users/kis/Documents/GitHub/coding-academy/dailywork/text.txt", "r")
# print(f.read())
A = f.read()
print(A)
B = A.replace("Python", "Java")
print(B)
f.close()



f = open("/Users/kis/Documents/GitHub/coding-academy/dailywork/text.txt", "w")
f.write(B)
f.close()

A = ["I", "love", "Python", "and", "Python"]
B = ""

for each in A:
    if each == "Python":
        A[A.index("Python")] = "Java"
    B = B + " " + each
print(B)
print(B.split())