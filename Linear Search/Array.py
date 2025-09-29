
from array import array

def search(list,n):
    for item in list:
        if item == n:
            return True
    return False

list = array('i',[1,2,3,4,5])
n = 5

if search(list,n):
    print("Found")
else:
    print("Not Found")






from array import array

def search(list,n):
    for i in list:
        return list.index(n)
    else:
        return -1

list = [1,2,3,4,5]
n = 5

result = search(list,n)
if result != -1:
    print(f"Found in {result}")
else:
    print("Not Found")
