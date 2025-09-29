


stack = [1,2,3,4,5]
print("Top Element :",stack[-1])
print("Popped :",stack.pop())
print("Stack after pop :",stack)
print("Is stack is empty :",len(stack) == 0)





def push():
    n = int(input("Enter the insert element : "))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)
        print(n,"is inserted into stack ")
        print()

def pop():
    if len(stack) == 0:
        print("STACK IS EMPTY")
    else:
        print(stack[0],"is deleted")
        del stack[0]
        print()

def display():
    if len(stack) == 0:
        print("STACK IS EMPTy")
    else:
        print("Element stacks are : ")
        for ele in stack:
            print(ele)
        print("Top of the stack is ",stack[0])

stack = []
while True:
    print("Enter the options below : ")
    print("1. PUSH OPERATION")
    print("2. POP OPERATION")
    print("3. DISPLAY OPERATION")
    print("ENTER ANY KEY TO EXIT. ")

    str = input()
    if str == '1':
        print("push operatioon")
        push()

    elif str == '2':
        print("pop operation")
        pop()

    elif str == '3':
        print("display operation")
        display()

    else:
        print("EXIT FROM PROGRAM")
        break

