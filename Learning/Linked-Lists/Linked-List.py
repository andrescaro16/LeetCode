class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
        

class LinkedList:
    
    def __init__(self):
        self.head = None


    def get_length(self):
        iterator = self.head
        counter = 0
        while iterator:
            counter += 1
            iterator = iterator.next
        return counter


    def print(self):
        if self.get_length() == 0:
            print("Linked list is empty")
            return

        iterator = self.head
        result = ''
        while iterator:
            if iterator.next != None:
                result += str(iterator.data) + '-->'
            else:
                result += str(iterator.data)
            iterator = iterator.next
        print(result)
    
    
    def insert_at_end(self, data):
        if self.get_length() == 0:
            self.head = Node(data)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data)
        return
    

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        return
    
    
    def insert_at(self, index, data):
        if (index < 0) or (index > self.get_length()):
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        
        counter = 0
        iterator = self.head
        while counter != index - 1:
            iterator = iterator.next
            counter += 1
        node = Node(data, iterator.next)
        iterator.next = node
        
        return


    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        counter = 0
        iterator = self.head
        while counter != index - 1:
            iterator = iterator.next
            counter += 1
        iterator.next = iterator.next.next
        return
    
    
    def insert_values(self, list, beginning = False):
        if len(list) == 0:
            raise Exception("The LinkedList is empty")
        
        if(beginning):
            list.reverse()
            for elem in list:
                self.insert_at_beginning(elem)
        else:
            for elem in list:
                self.insert_at_end(elem)
        
        return
    
    
    def insert_after_value(self, data_after, data_to_insert):
        iterator = self.head
        while iterator:
            if(iterator.data == data_after):
                node = Node(data_to_insert, iterator.next)
                iterator.next = node
                return
            iterator = iterator.next
        print("Value not found")
        return
        

    def remove_by_value(self, data):
        if self.get_length() == 0:
            print("The LinkedList is empty")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        iterator = self.head
        while iterator.next:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                return
            iterator = iterator.next
        print("Value not found")
        return

    
                
if __name__ == '__main__':
    linkedList = LinkedList()
    print("Length:", linkedList.get_length())
    linkedList.print()
    linkedList.insert_at_beginning(45)
    linkedList.insert_at_end(5)
    linkedList.insert_at_end(4)
    linkedList.insert_at_end(1)
    linkedList.insert_at_beginning(15)
    linkedList.print()
    linkedList.insert_at(3, 68)
    linkedList.print()
    linkedList.remove_at(0)
    linkedList.print()
    linkedList.insert_values([0, 2, 12])
    linkedList.print()
    linkedList.insert_after_value(1, 33)
    linkedList.print()
    linkedList.remove_by_value(4)
    linkedList.print()
    print("Length:", linkedList.get_length())
    
    