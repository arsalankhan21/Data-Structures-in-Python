"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
"""
# pylint: disable=W0212

# Imports
# Use any appropriate data structure here.
from List_array import List
from copy import deepcopy

# Constants
SEP = '-' * 40

class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, size):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of containing size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Parameter:
            size - number of initial slots in the hash table (int > 0)
        Returns:
            A new HashSet object (HashSet)
        -------------------------------------------------------
        """
        self._TableSize = size
        self._table = [None] * self._TableSize
        self._count = 0

        # Define the empty slots.
        for i in range(self._TableSize):
            self._table[i] = List()

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of elements in the HashSet.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of elements in the HashSet.
        -------------------------------------------------------
        """
        return self._count

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the HashSet is empty.
        Use: b = hs.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the HashSet is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _hashfunction(self, element):
        """
        -------------------------------------------------------
        Returns the index in the table where the element can
        be inserted.        
        Use: list = self._hashfunction(element)
        -------------------------------------------------------
        Returns:
            index - the position of the element in self._table
        -------------------------------------------------------
        """
        key = hash(element) #returns an integer key for the element 
        return key % self._TableSize        

    def __contains__(self, element):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains element.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            element - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        contains = False

        index = self._hashfunction(element)
        slot_table = self._table[index]
        if element in slot_table:
            contains = True

        return contains


    def insert(self, element):
        """
        ---------------------------------------------------------
        Inserts the given element into the Hash Set, allows only
        one copy of element        .
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(element)
        -------------------------------------------------------
        Parameters:
            element - a comparable data element (?)
        Returns:
            inserted - True if element is inserted, False otherwise.
        -------------------------------------------------------
        """
        
        index = self._hashfunction(element)
        slot_list = self._table[index]        
        if element in slot_list:
            # Do not insert data if already in hash set.            
            inserted = False
        else:
            inserted = True
            slot_list.insert(0, element)
            self._count += 1

            # Check the load factor and rehash if necessary.
            if self._count > (HashSet._LOAD_FACTOR * self._TableSize):
                self._rehash()
        
        return inserted

    def find(self, element):
        """
        ---------------------------------------------------------
        Returns the element identified by element.
        Use: element = hs.find(element)
        -------------------------------------------------------
        Parameters:
            element - a comparable data element (?)
        Returns:
            element - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        found = None
        index = self._hashfunction(element)
        slot_table = self._table[index]

        if element in slot_table:
            found = deepcopy(element)
        
        return found

     
    


    def remove(self, element):
        """
        ---------------------------------------------------------
        Removes the element matching the given element from the 
        Hash Set, if it exists.
        Use: element = hs.remove(element)
        -------------------------------------------------------
        Parameters:
            element - a comparable data element (?)
        Returns:
            element - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        found  = False
        index = self._hashfunction(element)
        slot_table = self._table[index]

        if element in slot_table:
            slot_table.remove(element)
            found = True
            self._count -= 1
        
        return found        

        
    
    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and
        reallocates the  existing data within the Hash Set to the
        new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        CHANGE_FACTOR = 2 * self._TableSize + 1    
        slots = CHANGE_FACTOR - self._TableSize    
        self._TableSize = CHANGE_FACTOR    
            
        for i in range(slots):    
            self._table.append(List())    
            
        for i in self._table:    
            for j in i:    
                if j is not None:    
                    h = hash(j)    
                    index = h % self._TableSize    
                    slot_table = self._table[index]    
                    if j not in slot_table:    
                        slot_table.insert(0,j)    
        return

        

        
    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = hs.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same elements
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """
        #your code here


    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the HashSet starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        #your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            element - the next element in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for element in slot:
                yield element
