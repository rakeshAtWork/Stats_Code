# Here we will implement linkedlist 


# inserting node at beging will take constant time complexity.

# operation becomes so easy and time complexity will be very geniune.


# here is the code for linkedlist 


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        