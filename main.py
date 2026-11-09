import os

print(os.environ["KEY"])

with open("test.txt", "w") as f:
    f.write(os.environ["KEY"])

with open("test.txt", "r") as f:
    a = f.readline()
    print(a)
