import datetime
import call

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, caller):
        self.calls.append(caller)
        self.queue_size = len(self.calls)
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue_size = len(self.calls)
        return self

    def remove_by_phone(self, phone_number):
        for idx in range(0, len(self.calls)):
            if self.calls[idx].phone == phone_number:
                self.calls.pop(idx)
                self.queue_size = len(self.calls)
                break
        return self

    def info(self):
        print "Waiting queue:", self.queue_size
        for caller in self.calls:
            # caller.display()
            print "Name:", caller.name
            print "Phone number:", caller.phone
            print ""
    def sort(self):
        # https://docs.python.org/2/library/functions.html
        # https://wiki.python.org/moin/HowTo/Sorting#Sortingbykeys
        self.calls.sort(key=lambda x: x.time_call, reverse=False)
        return self
    def __repr__(self):
        return "<CallCenter object Queue Size: {}>".format(self.queue_size)

if __name__ == "__main__":
    caller1 = call.Call("c1", "Toto", "123-123-1234", datetime.datetime.now(), "Reason1")
    caller2 = call.Call("c2", "Fata", "223-223-2234", datetime.datetime.now(), "Reason2")
    caller3 = call.Call("c3", "TDodo", "323-323-1234", datetime.datetime.now(), "Reason3")
    caller4 = call.Call("c4", "Anama", "443-424-2234", datetime.datetime.now(), "Reason4")
    caller5 = call.Call("c5", "Fnema", "453-524-5234", datetime.datetime.now(), "Reason5")

    cc1 = CallCenter()
    cc1.add(caller1).add(caller5).add(caller2).add(caller3).add(caller4)
    cc1.info()
    cc1.remove()
    cc1.remove_by_phone("323-323-1234")
    cc1.remove_by_phone("555-553-1234") # Do nothing
    cc1.info()
    cc1.sort().info()
    print cc1