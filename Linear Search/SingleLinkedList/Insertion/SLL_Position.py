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

    def position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos -1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

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

l.ending(90)       

l.position(3,25)     # 5 --> 10 --> 20 --> 25 --> 90 --> 
l.position(1,7)     # 5 --> 7 --> 10 --> 20 --> 25 --> 90 --> 

l.display() 



