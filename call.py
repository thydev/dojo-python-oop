import datetime

class Call(object):
    def __init__(self, uid, name, phone, time_call, reason):
        self.uid = uid
        self.name = name
        self.phone = phone
        self.time_call = time_call
        self.reason = reason
    def display(self):
        print "Unique ID:", self.uid
        print "Caller name:", self.name
        print "Phone number:", self.phone
        print "Time of call:", self.time_call
        print "Reason for call:", self.reason
        return self
    def __repr__(self):
        return "<Call object {} Phone:{} Time:{}>".format(self.name, self.phone, self.time_call)

if __name__ == "__main__":
    caller1 = Call("c1", "Toto", "123-123-1234", datetime.datetime.now(), "Reason1")
    caller2 = Call("c2", "Fata", "223-223-2234", datetime.datetime.now(), "Reason2")
    caller3 = Call("c3", "TDodo", "323-323-1234", datetime.datetime.now(), "Reason3")
    caller4 = Call("c4", "Anama", "443-424-2234", datetime.datetime.now(), "Reason4")
    caller5 = Call("c5", "Fnema", "453-524-5234", datetime.datetime.now(), "Reason5")
    print caller1
    print caller2
    print caller3
    print caller4
    print caller5

