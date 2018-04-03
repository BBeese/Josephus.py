class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    
    # Constructor
    def __init__(self):
        self.head = None

    def imminent_death(self,key,n):
        if self.head == None:
            return None
        
        current = self.head
        previous = self.head

        while previous.next != self.head:
            previous = previous.next
            
        while current.data != key:
            if current.next == self.head:
                return None
            previous = current
            current = current.next

        count = 1
        
        while (count != n):
            current = current.next
            count += 1

        return current.data

    # Insert an element (value) into the list
    def insert(self, item):
        newL = Link(item)

        if self.head == None:
            self.head = newL
            newL.next = self.head
            self.head = newL
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = newL
        newL.next = self.head
        newL.previous = current
            

    # Delete a link with a given key (value)
    def delete(self,key):
        if self.head == None:
            return None

        current = self.head
        previous = self.head
        
        while previous.next != self.head:
            previous = previous.next

        while current.data != key:
            if current.next == self.head:
                return None
            previous = current
            current = current.next

        if current == self.head:
            if self.head == self.head.next:
                self.head = None
                return current
            else:
                self.head = current.next
                
        previous.next = current.next
        return current

    def delete_after ( self, start, n ):
        if self.head == None:
            return None
        
        current = self.head
        while (current.data != start):
            current = current.next
            
        count = 1
        
        while (count != n):
            current = current.next
            count += 1

        #deleted = current.data
        self.delete(current.data)

        return current.next#, deleted

    def __str__(self):
        if self.head == None:
            return "None"
        else:
            ztring = "["
            current = self.head
            while current.next != self.head:
                ztring += str(current.data) + ","
                current = current.next
            ztring += str(current.data) + "]"
            return ztring

def main():

    with open ("josephus.txt", "r") as file:
        n = int(file.readline().strip())
        first = int(file.readline().strip())
        tick = int(file.readline().strip())

    soldiers = CircularList()

    # populate list with soldiers
    for i in range(1, n + 1):
        soldiers.insert(i)

    # print(soldiers) #testing the __str__ function

    # While the last link does not point to itsself
    while (soldiers.head.next != soldiers.head):
        rip = soldiers.imminent_death(first,tick)
        first = soldiers.delete_after(first, tick)
        first = first.data
        print(rip)

    print(soldiers.head.data)
    
main()
