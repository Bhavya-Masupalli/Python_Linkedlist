class Node:
    def __init__(self, value):
        self.info = value
        self.link = None
class Single_linked_list:
    def __init__(self):
        self.start = None
    def insert_at_end(self,data):
        temp = Node(data)
        if self.start == None:
            self.start = temp
            return
        else:
            p = self.start
            while p.link != None:
                p = p.link
            p.link = temp
    def create_list(self):
        n = int(input("enter the number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the elements to be entered: "))
            self.insert_at_end(data)
    def insert_at_front(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    def insert_after_node(self, data, x):
        temp = Node(data)
        p = self.start
        while p.link != None:
            if p.info == x:
               temp.link = p.link
               p.link = temp
            p = p.link
          
    def insert_before(self, data, x):
        temp = Node(data)
        
        if x == self.start.info:
            temp.link = self.start
            self.start = temp
        else:
             p = self.start
             while p.link != None:
                  if p.link.info == x:
                       temp.link = p.link
                       p.link = temp
                  p = p.link
       

    def insert_at_position(self,data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        p = self.start
        i = 1
        while i < k-1 and p.link != None:
            p = p.link
            i += 1
        if p.link == None:
            print ( "you can insert only upto position", i)
        else:
            temp.link = p.link
            p.link = temp
    def display_list(self):
        if self.start == None:
            print" linked list is empty"
        else:
            print"linked list is  "
            p = self.start
            while p!= None:
                print(p.info)
                p = p.link
    def delete_front(self):
        if self.start == None:
            print" linked list is empty"
            return
        else:
            self.start = self.start.link
    def delete_end(self):
        if self.start == None:
            print" linked list is empty"
        else:
            p = self.start
            while p.link.link != None:
                p = p.link
            p.link = None
    def delete_at_given_info(self, x):
        if self.start == None:
            print "linkde list is empty"
        else:
            p = self.start
            while p.link != None:
                if p.link.info == x:
                    p.link = p.link.link
                
                p = p.link
        
            

            
list = Single_linked_list()
list.create_list()
list.insert_at_end(5)
list.insert_after_node(50,7)
#list.delete_front()
#list.insert_before(66,7)
#list.delete_end()
list.delete_at_given_info(8)
list.display_list()
        
        
                
                
            
            
            
