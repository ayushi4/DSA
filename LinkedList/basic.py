class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printt(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''
    
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)
        
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
        
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def remove_at(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
            
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
        
    def insert_at_index(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            
            
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        if self.head == None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
    
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
                
            itr = itr.next
            
        
    def remove_by_value(self, data):
    # Remove first node that contains data
        if self.head == None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        found = 0
        while itr.next:
            
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            
            itr = itr.next
        
        if found == 0:
            print data, "is not found in list"
     
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","cherry","orange"])
    ll.printt()
    ll.insert_after_value("orange","apple") # insert apple after mango
    ll.printt()
    
    ll.remove_by_value("orange") # remove orange from linked list
    ll.printt()
    ll.remove_by_value("figs")
    ll.printt()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.printt()
