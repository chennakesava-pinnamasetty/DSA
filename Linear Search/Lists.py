
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i += 1
    return False

list = [1,2,3,4,5,6]
n = 6

if search(list,n):
    print("Found")
else:
    print("Not Found")






# Member ship


def search(list,n):
    return n in list

list = [1,2,3,4,5]
n = 51

if search(list,n):
    print("Found")
else:
    print("Not Found")





# For loop

def search(list,n):
    for item in list:
        if item == n:
            return True
    return False

list = [1,2,3,4,5]
n = 4

if search(list,n):
    print("Found")
else:
    print("Not Found")




# INDEX NUMBER

def search(list,n):
    i = 0
    while i < len(list):
     if  list[i] == n:
        return i
     i += 1
    return -1

list = [1,2,3,4,5]
n = 2

result = search(list,n)
if result != -1:
    print(f"Found in {result}")
else:
    print("Not Found")