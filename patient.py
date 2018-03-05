class Patient(object):
    def __init__(self, uid, name, allergy):
        self.uid = uid
        self.name = name
        self.allergy = allergy
        self.bed_number = ""
    def __repr__(self):
        return "<Patient Object {} UID: {}>".format(self.name, self.uid)