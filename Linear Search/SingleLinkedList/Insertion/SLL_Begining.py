class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next



l = SLL()

n = Node(10)
l.head = n

n1 = Node(20)
l.head.next = n1

n2 = Node(30)
n1.next = n2

l.insert_begining(5)   # 5 --> 10 --> 20 --> 30 --> 
l.insert_begining(3)   # 3 --> 5 --> 10 --> 20 --> 30 --> 

l.display()
        