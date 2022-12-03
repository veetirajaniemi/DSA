def hash(x):
    sum = 0
    for i in range(0, len(x)):
        sum = sum + ord(x[i])
    return sum % 5

print(hash("dog"))
print(hash("cat"))
print(hash("bird"))
print(hash("worm"))
print(hash("fish"))
print(hash("cow"))
print(hash("wolf"))
print(hash("fox"))
print(hash("seal"))
print(hash("fly"))