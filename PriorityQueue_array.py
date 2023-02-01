"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
"""
# pylint: disable=W0212

# Imports
from copy import deepcopy


class PriorityQueue:

    DEFAULT_SIZE = 60
    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Returns:
            a new PriorityQueue object (PriorityQueue)
        -------------------------------------------------------
        """
                    
        assert max_size > 0, "List size must be > 0"
        self._capacity = max_size
        self._values = [None] * self._capacity
        self._count = 0
        self._first = None
                

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.isEmpty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0
    
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of elements in the priority queue.
        -------------------------------------------------------
        """
        return self._count


    def insert(self, element):
        """
        -------------------------------------------------------
        A copy of element is appended to the end of the the 
        Python list storing the data in the Priority Queue, and
        _first is updated as appropriate to the index of
        element with the highest priority.
        Use: pq.insert(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._count < self._capacity, "Priority queue is full"
        self._values[self._count] = deepcopy(element)
        self._count += 1
        self._set_first()
        return
                      

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the element of _first.
        _first is the index of the element with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        #your code here

        n = self._count

        if n == 0:
            self._first = None
        else:
            self._first = 0

            for i in range(1, n):
                if self._values[i] < self._values[self._first]:
                    self._first = i
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority element from the priority queue.
        Use: element = pq.remove()
        -------------------------------------------------------
        Returns:
            element - the highest priority element in the priority queue -
                the element is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        
        assert self._count > 0, "Cannot remove from an empty priority queue"
        element = deepcopy(self._values[self._first])
        self._count -= 1
        self._values[self._first] = self._values[self._count]
        self._set_first()
        return element

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority element of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            element - a copy of the highest priority element in the priority queue -
                the element is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"
        element = deepcopy(self._values[self._first])
        return element


    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a Priority Queue into two with elements going into
        alternating Priority Queues. The current Priority Queue
        is empty when the method ends. The order of the elements
        in current Priority Queue is preserved.
        Use: target1, target2 = pq.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a Priority Queue that contains alternating 
                elements from the current Priority Queue (PriorityQueue)
            target2 - a Priority Queue that contains alternating 
                elements from the current Priority Queue (PriorityQueue)
        -------------------------------------------------------
        """ 
        
        target1 = PriorityQueue()
        target2 = PriorityQueue()

        for i in range(self._count):
            if i % 2 == 0:
                target1.insert(self._values[i])
            else:
                target2.insert(self._values[i])

        self._count = 0
        self._first = None

        return target1, target2



     


    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a Priority Queue into two depending on an external
        key. The current Priority Queue (pq) will be empty when the 
        method ends. The elements smaller than than key 
        go into target1 and the elements larger than key go into
        target2. The order of the elements from current 
        Priority Queue (pq) is preserved.
        Use: target1, target2 = pq.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            target1 - a priority queue that contains all elements
                with priority higher than key (PriorityQueue)
            target2 - priority queue that contains all elements with
                priority lower than or equal to key (PriorityQueue)
        -------------------------------------------------------
    """

        target1 = PriorityQueue()
        target2 = PriorityQueue()

        for i in range(self._count):
            if self._values[i] < key:
                target1.insert(self._values[i])
            else:
                target2.insert(self._values[i])

        self._count = 0
        self._first = None

        return target1, target2
        

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
