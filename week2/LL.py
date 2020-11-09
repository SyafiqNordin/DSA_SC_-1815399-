# node class
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    # method to update the data of the Node
    def updateData(self, data):
        self.data = data

    # method to set Link for the Next Node
    def setLink(self, node):
        self.link = node

    # method returns data stored in the Node
    def getData(self):
        return self.data

    # method returns address of the next Node // goes to the Next Node
    def getNextNode(self):
        return self.link

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # method adds elements to the left of the Linked List
    def addToStart(self, data):# 21
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode
    #method of finding first k elements
    def firstK(self,k):
        start=self.head
        i=0
        while i<k:
            print(str(start.getData()),end=" ")
            i=i+1
            start=start.link
            if start and i<k :
                print("-->",end=" ")
        
        print()

    # method of reversing elements without creating new one
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.link
            current.link = prev
            prev = current
            current = next
        self.head = prev

    # method of pushing O(1)
    def insertAfter(self, prev_node, new_data):
  
        if prev_node is None: 
            return
  
        new_node = Node(new_data) 
        new_node.link = prev_node.link
        prev_node.link = new_node   


    # method of copying elements to a new linkedlist object
    def copy(self)

        start=self.head
        while start:
            
    #method to convert linkedlist to list
    def convert(self):
        start=self.head
        list=[]
        while start:
            list.append(start.getData())
            start=start.link

        return list


    # method adds elements to the right of the Linked List
    def addToEnd(self, data): # data = 16
        start = self.head
        tempNode = Node(data) # data = 16 : link = None
        # start  = 5
        # reach the last element TAIL
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start:# start != None
            size += 1
            start = start.getNextNode()
        # print(size)
        return size

    # method returns index of the recieved data
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()


    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

    # method removes and returns the last element from the Linked List
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data

    # method to clear LinkedList
    def clear(self):
        self.head = None
        return True


    # method returns count of Element recieved
    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1




# creating LinkedList
myList = LinkedList()

# adding some elements to the start of LinkedList
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
# 1 -> 2 -> 3 -> 4 -> 5 -> None

myList.display()



# adding some elements to the End of the LinkedList
myList.addToEnd(12)
myList.addToEnd(13)
myList.addToEnd(3)
myList.display()
# 1 -> 2 -> 3 -> 4 -> 5 -> 13 -> 3 -> 31
# printing Length
print(myList.length())

# printing index of an element
print(myList.index(12))

# removing an element
print(myList.remove(12))

myList.display()

# printing max and min element
print(myList.Max())
print(myList.Min())

# pushing and poping elements
print(myList.push(31))
myList.display()
print(myList.pop())
myList.display()

# printing count of particular element in the List
print(myList.count(3))


# printing first k elements
print("insert value K :")
k=int(input())
myList.firstK(k)


#printing reversed elements
myList.reverse()
myList.display()


#push in O(1)
print("pushing in O(1)")
myList.insertAfter(myList.head.link, 8)
myList.display()


#copy linkedlist into a new object
myList1 = LinkedList()

mylist1.



#printing list from linkedlist
print("converting to list")
normallist=myList.convert()
print(normallist)
