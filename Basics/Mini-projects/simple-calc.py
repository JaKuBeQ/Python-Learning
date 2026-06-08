def div(a,b):
    return a/b

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

print("choose number: ")
a = int(input())
print("what you want to do? add/sub/mul/div ")
c = input()
print("choose second number: ")
b = int(input())
if c == "add":
    print(add(a,b))
elif c == "sub":
    print(sub(a,b))
elif c == "mul":
    print(mul(a,b))
elif c == "div":
    print(div(a,b))
else:
    print("wrong input")