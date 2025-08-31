'''
In this module, we are going to be using the Iterator Design Pattern in our code.
This is going to be a very simple example to show using the Iterator Design Pattern more clear.

The Iterator Design Pattern is a widely used Design Pattern in software development that provides a way to access the elements of an aggregate object (such as a list or collection) sequentially without exposing its underlying  representation.
Note: This is going to be Iterator Design Pattern, it means all the classes in this file are iterator(not iterable). So you can just run while loops on them(not for loops).

You can read more about this Design Pattern from this url: https://www.geeksforgeeks.org/system-design/iterator-pattern/
'''


# This is a class that is used to make iterator objects(So this is using the iterator design pattern).
class Iterator:
    def __init__(self, items: list | tuple) -> None:
        self.items = items # All the items that should be iterated.
        self.index = 0 # The index of the specific item(that is being iterated).

    # A method to return the next item from the items list(or tuple or set).
    def next(self) -> any:
        if self.has_next(): # Checking if there is another item,
            self.index += 1
            return self.items[self.index - 1]
        else:
            raise StopIteration('The iterations has stopped.') # If there is not more items, then this error will be raised.
        
    def has_next(self):
        if self.index < len(self.items):
            return True
        return False
    
    # A method to reset the index(for more iterations from the object).
    def reset(self) -> None:
        self.index = 0
    

# Testing the Iterator class.
if __name__ == '__main__':
    obj1 = Iterator([1, 2, 3, 4, 5]) # The object is created with a list including numbers 1 to 5.

    # Testing the performance of `Iterator.next()` method.
    print('\n\n\n')
    print(obj1.next())
    print(obj1.next())
    print(obj1.next())
    print(obj1.next())
    print(obj1.next())

    # Testing the performance of `Iterator.reset()` method(We are resetting the object to iterate it again).
    obj1.reset()
    print()

    # Iterate the object again(this time using while).
    while obj1.has_next():
        print(obj1.next())
    # print(obj1.next()) # If we run the code with this line, we are going to get an StopIteration error(Raised from Iterator.next()).



print('\n\n')



# This class is exactly the same as the `Iterator` class, but it is written to show how to use Iterator Design Pattern in a more pythonic way.
class PythonicIterator:
    def __init__(self, items: list | tuple) -> None:
        self.items = items
        self.index = 0

    # Using the `__iter__()` dunder method is exactly like this. See: https://www.geeksforgeeks.org/python/python-__iter__-__next__-converting-object-iterator/
    def __iter__(self):
        return self
    
    # Using the `__next__()` dunder method allows you to run the `next()` builtin function on the object. This way is more recommended if you are programming in python.
    def __next__(self):
        if self.has_next():
            self.index += 1
            return self.items[self.index - 1]
        else:
            raise StopIteration('The iterations has stopped.')
        
    def has_next(self):
        if self.index < len(self.items):
            return True
        return False
        
    def reset(self):
        self.index = 0
    

# Testing the PythonicIterator class.
if __name__ == '__main__':
    obj2 = PythonicIterator(['A', 'B', 'C', 'D', 'E']) # The object is created with a list including letters A to E.

    # Testing the performance of `PythonicIterator.__next__()` dunder method. The `PythonicIterator.__next__()` allows you to iterate the next item using the `next()` builtin function that is more common in python.
    print(next(obj2))
    print(next(obj2))
    print(next(obj2))
    print(next(obj2))
    print(next(obj2))

    obj2.reset()
    print()

    while obj2.has_next():
        print(next(obj2))
    # print(next(obj2)) # If we run the code with this line, we are going to get an StopIteration error(Raised from PythonicIterator.__next__()).
    print('\n\n\n')
