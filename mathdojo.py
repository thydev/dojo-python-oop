class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self, num1, *args):
        if type(num1) is list:
            self.result += sum(num1)
            if len(args) > 0:
                for v in args:
                    if type(v) is list:
                        self.result += sum(v)
                    else:
                        self.result += v
        else:
            self.result += num1
            if len(args) > 0:
                for v in args:
                    if type(v) is list:
                        self.result += sum(v)
                    else:
                        self.result += v
        return self

    def subtract(self, num1, *args):
        if type(num1) is list:
            self.result -= sum(num1)
            if len(args) > 0:
                for v in args:
                    if type(v) is list:
                        self.result -= sum(v)
                    else:
                        self.result -= v
        else:
            self.result -= num1
            if len(args) > 0:
                for v in args:
                    if type(v) is list:
                        self.result -= sum(v)
                    else:
                        self.result -= v
        return self

md = MathDojo()
md.add(2, 3, 2, 1).subtract(2, 1, 1).subtract(1)
print md.result

md.result = 0
md.add(2).add(2, 5).subtract(3, 2)
print md.result

md.result = 0
md.add([2]).add([2, 1, 1], [5, 2], 5).add(2, 5).subtract(3, 2)
print md.result

md.result = 0
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3])
print md.result