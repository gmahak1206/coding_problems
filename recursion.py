def num(n):
    if n == 1:
        print(1,end=" ")
        return 
    num(n-1)
    print(n , end=" ")

def num_rev(n):
    if n == 0:
        return 
    print(n , end = " ")
    num_rev(n-1)

def array(arr , i):
    if i == len(arr):
        return 
    print(arr[i] , end = " ")
    array(arr , i+1)

def array_rev(arr , i):
    if i < 0:
        return 
    print(arr[i], end = " ")
    array_rev(arr , i-1)

def maxa2(arr , i):
    if i == len(arr)-1:
        return arr[i]
    maxa = max(arr[i] , maxa2(arr , i+1))
    return maxa

def mina2(arr , i):
    if i == len(arr)-1:
        return arr[i]
    mina = min(arr[i] , mina2(arr , i+1))
    return mina

num(5)
print()
num_rev(5)
print()
array([6,7,8,9,0] , 0)
print()
array_rev([6,7,8,9,0] , 4)
print()
print(maxa2([6,7,8,9,0] , 0))
print(mina2([6,7,8,9,0] , 0))
print()