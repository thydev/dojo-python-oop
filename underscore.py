class Underscore(object):
    def map(self, lst, callback):
        new_lst = []
        for v in lst:
            new_lst.append(callback(v))
        return new_lst
        
    def reduce(self, lst, callback):
        while len(lst) > 1:
            lst[1] = callback(lst[0], lst[1])
            lst.pop(0)
        return lst[0]

    # Looks through each value in the list, returning the first one that passes a truth test 
    def find(self, lst, callback):
        for v in lst:
            if callback(v):
                return v
        # Not found
        return -1
    def filter(self, lst, callback):
        new_lst = []
        for v in lst:
            if callback(v):
                new_lst.append(v)
        return new_lst        
    def reject(self, lst, callback):
        # Returns the values in list without the elements that the truth test (predicate) passes. The opposite of filter.
        new_lst = []
        for v in lst:
            if callback(v) == False:
                new_lst.append(v)
        
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code ab
print "Evens:", evens
odds = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2)
print "Odd:", odds

square = _.map([3, 2, 5, 7], lambda x: x * x)
print "square:", square
celsius = _.map([70, 65, 45, 90], lambda x: (float(5)/9)*(x-32))
print "celsius:", celsius

sum = _.reduce([3, 2, 1], lambda a, b: a + b)
print "Sum:", sum
max = _.reduce([3, 43, 2, 41, 44, 9, 10], lambda a, b: a if (a >b) else b)
print "Max:", max

firstodds = _.find([2, 3, 4, 5, 6], lambda x: x % 2)
print "First odd:", firstodds

firstodds = _.find([2, 30, 4, 50, 6], lambda x: x % 2)
print "First odd:", firstodds

evens2 = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2)
# should return [2, 4, 6] after you finish implementing the code ab
print "Evens2:", evens
odds2 = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "Odd2:", odds