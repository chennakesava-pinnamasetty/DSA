

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next


    

    def Del_End(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None


l = SLL()

n = Node(10)
l.head = n

n1 = Node(20)
l.head.next = n1

n2 = Node(30)
n1.next = n2

n3 = Node(40)
n2.next = n3          # 10 --> 20 --> 30 --> 40 --> 



l.Del_End()         # 10 --> 20 --> 30 --> 

l.Del_End()         # 10 --> 20 --> 
 
l.display()