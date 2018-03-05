
class Patient(object):
    def __init__(self, uid, name, allergy):
        self.uid = uid
        self.name = name
        self.allergy = allergy
        self.bed_number = ""

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
    
    def admit(self, patient, bed_number):
        if len(self.patients) >= self.capacity:
            return "The hospital is full"
        else:
            patient.bed_number = bed_number
            self.patients.append(patient)
            return "Successfully added!"
        
    def discharge(self, p_uid):
        for idx in range(0, len(self.patients)):
            if self.patients[idx].uid == p_uid:
                self.patients[idx].bed_number = "" 
                self.patients.pop(idx)
                break
        
        return self
    def display_info(self):
        for p in self.patients:
            print "Patient: ", p.name
            print "Allergy:", p.allergy
            print "Bed number:", p.bed_number
            print ""

        return self

p1 = Patient("p1", "Dodo", "Milk")
p2 = Patient("p2", "CoCo", "Coffe")
p3 = Patient("p3", "Sodo", "Cheese")
p4 = Patient("p4", "FoFo", "Banana")
p5 = Patient("p5", "Vodo", "Apple")

h = Hospital("Ever Green", 3)
h.admit(p1, "bed101")
h.admit(p2, "bed201")
h.admit(p3, "bed1234")
h.admit(p4, "bed1235")
h.admit(p5, "bed1236")

h.discharge("p3")
h.display_info()