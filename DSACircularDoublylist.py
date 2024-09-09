class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CircularDoublyList:
    def __init__(self):
        self.head=None
    def append (self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.next=new_node
            self.prev=new_node
            self.length=1
        new_node.next=self.head
        new_node.prev=self.tail
        self.head.prev=new_node
        self.tail.next=new_node
        self.tail=new_node
        self.length+=1
    def prepend (self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.next=new_node
            self.prev=new_node
            self.length=1
        new_node.next=self.head
        new_node.prev=self.tail
        self.head.prev=new_node
        self.tail.next=new_node
        self.head=new_node
        self.length+=1
    def popfirst(self):
        if self.head is None:
            return None
        temp=self.head
        self.tail.next=temp.next
        self.head=temp.next
        self.head.prev=self.tail
        self.length-=1
    def poplast(self):
        if self.head is None:
            return None
        temp=self.head
        for _ in range(self.length+1):
            temp=temp.next
        temp.next=self.head
        self.head.prev=temp
        self.tail=temp
        self.length-=1
    def delete (self,index):
        if index==0:
            self.popfirst()
        if index==self.length:
            self.poplast()
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range (index-1):
            temp=temp.next
        after=temp.next
        temp.next=after.next
        after.next.prev=temp
        self.length-=1
        

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            if temp==self.head:
                break
CL=CircularDoublyList()
CL.append(1)
CL.append(2)
CL.append(3)
CL.prepend(5)
CL.prepend(9)
CL.delete(3)
CL.printlist()