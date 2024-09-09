class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self, data):
        new_node=Node(data)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,"-->")
            temp=temp.next
    def append (self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(data)
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def poplist (self):
        temp=self.head
        if self.length==0:
            return None
        for _ in range(self.length-1):
            temp=temp.next
        temp.next=None
        self.tail=temp
        self.length-=1
ll=Linked_list(2)
ll.append(3)
ll.append(4)
ll.poplist()
ll.printlist()
        