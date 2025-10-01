
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None                                            

class SLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty ")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next 
            

l = SLL()
n = Node(10)
l.head = n

n1 = Node(20)
l.head.next=n1

n2 = Node(30)
n1.next = n2

l.display()

        