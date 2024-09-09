class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.next=self.head
            self.tail=self.head
            self.length=1
        else:
            temp=self.head
            new_node.next=self.head
            self.tail.next=new_node
            self.tail=new_node

    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.next=self.head
            self.tail=self.head
            self.length=1
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
            self.length+=1
    def insert(self,data,index):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.next=self.head
            self.tail=self.head
            self.length=1
        if index<0 or index>=self.length:
            return "Index out of range"
        temp=self.head
        for _ in range (index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
    def popfirst(self):
        if self.head is None:
            return "List is empty"
        temp=self.head
        self.tail.next=temp.next
        self.head=temp.next
        self.length-=1
    def poplast(self):
        if self.head is None:
            return "List is empty"
        temp=self.head
        for _ in range (self.length):
            temp=temp.next
        temp.next=self.head
        self.tail.next=None
        self.tail=temp
        self.length-=1
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break
CL=CircularList()
CL.append(1)
CL.append(2)
CL.append(3)
CL.prepend(-2)
CL.prepend(-1)
CL.insert(-3,2)
CL.poplast()
CL.popfirst()
CL.printlist()