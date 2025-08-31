'''
In this module, we are going to be using the Singleton Design Pattern in our code.
This is going to be a very simple example to show using the Singleton Design Pattern more clear.

The Singleton Method Design Pattern ensures a class has only one instance and provides a global 
access point to it.

You can read more about this Design Pattern from this url: https://www.geeksforgeeks.org/system-design/singleton-design-pattern/ 
'''


from threading import Lock


# This is a class that is used to print an important text prettier. This class is using the singleton Design Pattern. 
class SingletonDesignPattern:
    _instance = None
    _initialized = False

    def __new__(cls):
        lock = Lock()
        # Using `threading.Lock` will help the class to run correctly when using multithreading.
        with lock:
            if cls._instance is None: # If the class has no instance(`cls._instance` will be None).
                return super().__new__(cls)
            # If the class has one instance, the new one will be assigned to the first instance.
            return cls._instance 
    
    def __init__(self):
        if self._initialized is False: # If the object isn't already initialized,
            self.set_obj(self)
            print(f'\n** Object with id {id(self._instance)} initializes successfully **\n')

    # This method sets the cls._instance and cls._initialized to specify that there is an instance made from this class.
    @classmethod
    def set_obj(cls, obj: object):
        cls._instance = obj
        cls._initialized = True
        return cls._instance

    # A method to do the main task of the class.
    def customized_print(self, text: str):
        if self._instance and self._initialized: 
            temp_list = text.split(' ')
            temp_list = [ i.capitalize() for i in temp_list ]
            result = ' '.join(temp_list)
            return f'\n\n{result}\n\n'

    # A method to close the instance.
    # This is a classmethod to be able to access the `cls`.
    @classmethod
    def close(cls):
        if cls._instance is not None: # If the instance isn't already closed,
            print(f'\n** Object with id {id(cls._instance)} closed successfully **\n')
            cls._instance = None
            cls._initialized = False
        else: # The instance is already closed.
            raise RuntimeError('This object has already closed.')
        
    def __str__(self):
        if self._instance is not None:
            return str(id(self._instance))
        else:
            return '!! Closed object !!'
    

obj1 = SingletonDesignPattern() # The first object from the class(It's accepted).
obj2 = SingletonDesignPattern() # The second object from the class(Not accepted, will be `obj1`).

print(obj1.customized_print('hello world!')) # Running a method from the class(using the object).
print(obj1 is obj2) # This line shows that both `obj1` and `obj2` are exactly the same.

obj1.close() # Closing `obj1`.
# obj2.close() # If we run the code with this line, we are going to receive a RuntimeError(close method, raise part).
