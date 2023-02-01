"""
-------------------------------------------------------
Circular array version of the Queue ADT.
-------------------------------------------------------
"""
# pylint: disable=W0212

from copy import deepcopy



class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 50

    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size 
        Python list.
        Use: queue = Queue(max_size)
        Use: queue = Queue()  # uses default max size
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"

        self._capacity = max_size
        self._values = [None] * self._capacity
        self._front = 1
        self._rear = 0
        self._count = 0

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = queue.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = queue.isFull()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return self._count == self._capacity

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        return self._count

    def enqueue(self, element):
        """
        -------------------------------------------------------
        Adds a copy of the element to the rear of the queue.
        Use: queue.enqueue( element )
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert not self.isFull(), "Queue is full"

        self._rear = (self._rear + 1) % self._capacity
        self._values[self._rear] = deepcopy(element)
        self._count += 1
        return

    def dequeue(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = queue.dequeue()
        -------------------------------------------------------
        Returns:
            element - the data element at the front of the queue is 
            returned, the data element is removed from the queue (?)
        -------------------------------------------------------
        """
        assert not self.isEmpty(), "Cannot remove from an empty queue"

        value = self._values[self._front]
        self._values[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._count -= 1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        returns the value at the front of queue without removing it
        Use: v = queue.front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[self._front])
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        j = self._front
        i = 0

        while i < self._count:
            yield self._values[j]
            i += 1
            j = (j + 1) % self._capacity
            
            
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a Queue into two with values going to
        alternating queues. The self Queue is empty when the
        method ends. The order of the values from self is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a Queue that contains alternating values
                from the current Queue (Queue)
            target2 - a Queue that contains other alternating
                values from  the current Queue (Queue)
        -------------------------------------------------------
        """  
        target1 = Queue()
        target2 = Queue()
        right = True 
        n = self._count
        
        for i in range(n):
            
            if right:
                target1.enqueue(self.dequeue())
            else:
                target2.enqueue(self.dequeue())
            right = not right 
        
        return target1, target2
    
            
            
        
            
            
          
