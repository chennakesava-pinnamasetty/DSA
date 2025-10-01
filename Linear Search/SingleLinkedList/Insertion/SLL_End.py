class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def Begining(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def ending(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def display(self):
        if self.head is None:
            print("List is Empty")
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

l.Begining(5)

l.ending(90)        # 5 --> 10 --> 20 --> 90 --> 

l.display()



