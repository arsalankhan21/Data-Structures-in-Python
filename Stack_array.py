"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------

"""
# pylint: disable=W0212

from copy import deepcopy

class Stack:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 8

    def __init__(self, max_size = DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a 
        fixed-size Python list.
        
        Use: stack = Stack(max_size)
        Use: stack = Stack()    # uses default max size
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the Stack (int > 0)
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        
        assert max_size > 0, "Queue size must be > 0" #Creates assertion to that error was made because max size was less than zero
 
        self._capacity = max_size #self._capacity must be equal to the max_size parameter defined above
        self._values = [None] * self._capacity #self._values equals {none} times the max size - so 8 None values
        self._top = -1 # Counter that starts at negative one and makes its way up as contents of the stack is added, the top value of a stack

    def isEmpty(self): # Defines if stack is empty - if it is empty it will return True, if not return False
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return self._top == -1

        #self._top is originally set as -1, if it is -1, it means there are no contents added to the stack, therefore stack is empty
        
        
        
    
    def isFull(self): # Determines if stack is full, if stack is full this function will return True, if stack is not full it will return false
        """
        -------------------------------------------------------
        Determines if the stack is full.
        Use: b = stack.isFull()
        -------------------------------------------------------
        Returns:
            True if stack is full, False otherwise
        -------------------------------------------------------
        """
        return self._top == self._capacity - 1
    
        # If the top value of stack is equal to the max_size minus 1 because self._top starts at -1, it will prove that stack is full

    def push(self, element):
        """
        -------------------------------------------------------
        Pushes a copy of the given element onto the top of the 
        stack.
        Use: stack.push(element)
        -------------------------------------------------------
        Parameters:
            element - the data element to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert not self.isFull(), "Stack is full"
        
        self._top += 1
        self._values[ self._top ] = deepcopy( element )
        return
        
        # Increments self._top by 1 as there will be a new content added to stack
        #At the top value of stack - first value being self._values[0] and top being self._values[self._top]
        # That is currently an empty space, in the empty space put in a deepcopy of the element in which you would like to input in your stack
    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The data element is 
        removed from the stack. Attempting to pop from an empty 
        stack throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert not self.isEmpty(), "Cannot pop from an empty stack"

        value = deepcopy( self._values[ self._top ] )
        self._values[ self._top ] = None
        self._top -=1
        return value
    
        #Pops a copy of the stack and replaces copy with None
        # self._top is not decremented by 1 and stack has lost a value 
        

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack without
        removing it.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        
        assert not self.isEmpty(), "Cannot peek at an empty stack"

        value = deepcopy(self._values[self._top])
        
        return value
        
        
        # This function will view the stack from above and peek at the top value of the stack
        #Attempting to peek at an empty stack will cause an assertion error
        # value equals the deepcopy version of the element at the top of the stack 

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source1._capacity == source2._capacity, \
            "Stack capacities must be the same" 

        self._capacity = source1._capacity #source 
        self._values = [None] * self._capacity
        self._top = -1

        while not source1.isEmpty() and not source2.isEmpty():
            self.push(source1.pop())
            self.push(source2.pop())
        return
    
        
        
        

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into two separate target stacks 
        with values alternating into the targets. At finish 
        source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack(self._capacity)
        target2 = Stack(self._capacity)
        while not self.isEmpty():
            target1.push(self.pop())
            if not self.isEmpty():
                target2.push(self.pop())
        return target1, target2

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for value in stack:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
