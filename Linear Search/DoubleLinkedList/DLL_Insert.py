

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


# SLL Begining is more difficlut in this

# DLL
    def Begining_insert(self,data):
        nb = Node(data)
        temp = self.head
        temp.prev = nb
        nb.next = temp
        self.head = nb

# Chatgpt
    def Beg(self,data):
        nb = Node(data)
        if self.head is not None:
            nb.next = self.head
            self.head.prev = nb
        self.head = nb

# SLL
    def ending(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

#DLL
    def endinggg(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp

# SLL
    def position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos -1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

# DLL
    def positionnnnnn(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos -1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next.prev = np
        temp.next = np



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
n2.next = n3           # 10 --> 20 --> 30 --> 40 --> 

l.Begining_insert(5)     # 5 --> 10 --> 20 --> 30 --> 40 --> 
l.Begining_insert(3)     # 3 --> 5 --> 10 --> 20 --> 30 --> 40 --> 

#l.Beg(3)


l.endinggg(70)     # 10 --> 20 --> 30 --> 40 --> 70 --> 

l.positionnnnnn(2,444)       # 3 --> 5 --> 444 --> 10 --> 20 --> 30 --> 40 --> 70 --> 

l.display()