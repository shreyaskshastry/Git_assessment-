def add(a,b):
    return a+b 

def sub(a,b):
    return a-b

def div(a,b):
    if(b == 0):
        return -1
    return a/b

def mul(a,b):
    return a*b

def pow(a,b):
    return a^b

print(add(2,3))
print(sub(4,2))
print(div(10,2))
print(mul(2,3))
print(pow(2,4))