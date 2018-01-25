class Node(object):

    def __init__(self,prev,element,next):
        self.prev = prev
        self.element = element
        self.next = next

class List(object):
    head = Node(None, None, None)
    tail = Node(None, None, None)
    head.next = tail
    tail.prev = head
   
    count = 0

    def add(self,element):
        new_node = Node(None, element, None)
        if self.head.next == self.tail:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.prev = self.head
            new_node.next = self.tail
        else:
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node
            
        self.count += 1
    
            
    def remove(self,value):
        current_node = self.head.next
        while current_node is not self.tail:
            if current_node.element == value:
                if current_node.prev is self.head:
                    self.head.next = self.tail
                    self.tail.prev = self.head
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                self.count -= 1
            current_node = current_node.next           
                

    def show(self):
        current_node = self.head.next
        while current_node is not self.tail:
            print(current_node.element)
            current_node = current_node.next
        print("number of entries : "+ str(self.count))

    def sort(self):
        jnode = self.head.next.next
     
        if jnode is self.tail:
            print("there is only one element")
            return
            
        if jnode is None:
            print("there is no element in this linked list")
            return
        
       
        
        while jnode is not self.tail:
            inode = jnode.prev
            while inode is not self.head:
                if inode.element > jnode.element:
                    inode.next = jnode.next
                    jnode.prev = inode.prev
                    inode.prev.next = jnode
                    jnode.next.prev= inode
                    jnode.next = inode
                    inode.prev = jnode
                inode = inode.prev
            jnode = jnode.next
        
        


d = List()
d.add(4)
d.add(6)
d.add(9)
d.add(1)
d.add(13)
d.add(4)
d.add(2)
d.sort()
d.show()


                