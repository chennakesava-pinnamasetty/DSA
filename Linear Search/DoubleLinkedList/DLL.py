class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None



    def display(self):
        if self.head is None:
            print("Double Link is Empty")
        else:
            temp = self.head
            while temp:
                
                print(temp.data,"-->",end=" ")
                temp = temp.next



l = DLL()

n = Node(10)
l.head = n 

n1 = Node(20)
l.prev = n1
n.next = n1

n2 = Node(30)
l.prev = n2
n1.next = n2


n3 = Node(40)
l.prev = n3
n2.next = n3


l.display()         # 10 --> 20 --> 30 --> 40 --> 