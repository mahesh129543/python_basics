class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

# a=Node(1)

# print(a)/

class linklist:
    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n

    def Insert_head(self, value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1

    def Travles(self):
        curr=self.head
        while curr!=None:
            print(curr.data,"->",end=" ")
            
            curr=curr.next


    print("\n")

    def insert_tail(self,value):

        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node

    def insertmiddle(self,value,after):
        new_node=Node(value)
        curr=self.head
        while curr != None:
            if curr.data==after:
                break
            curr=curr.next

        if curr != None:
            new_node.next=curr.next
            curr.next=new_node
        else:
            print("not found")

    def deletehead(self):
        if self.head!=None:
            self.head=self.head.next
            self.n=self.n-1
        else:
            print("list is empty")
            



L= linklist()
L.Insert_head(1)
L.Insert_head(2)
L.Insert_head(3)
L.Insert_head(4)
print(len(L))
L.Travles()
L.insert_tail(5)
print("mah")
L.Travles()
print("at middle")

L.insertmiddle(45,4)
L.Travles()

L.deletehead()
L.Travles()