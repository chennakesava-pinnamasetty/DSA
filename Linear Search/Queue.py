

def enqueue():
    n = int(input("Enter a number : "))
    queue.append(n)
    print()

def dequeue():
    if len(queue) == 0:
        print("Queue is empty ")
    else:
        print(queue[0],"is deleted")
        del queue[0]
    print()

def display():
    if len(queue) == 0:
        print("Queue is empty")
        print("------------------")
        print()
    else:
        print("Elements are : ")
        for ele in queue:
            print(ele,end=" ")
        print("\nFront of the queue ",queue[0])
        print("Rear of the queue",queue[-1])


queue = []

while True:
  print("Enter below oerations :")
  print("1.Enqueue operatiom ")
  print("2. Dequeue operation ")
  print("3. Display operation ")
  print("4.Exit the program ")
  
  str = input()
  if str == '1':
      print("Enqueue Operation ")
      enqueue()
  
  elif str == '2':
      print("Dequeue operation ")
      dequeue()
  
  elif str == '3':
      print("Display : ")
      display()
  
  else:
      print("Exit the program ")