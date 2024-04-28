# single inheritance
class box:
    def _init_(self,nameOfStudent,rollNo):
        self.nameOfStudent=nameOfStudent
        self.rollNo=rollNo

class box2(box):
    def _init_(self,marks):
        self.marks=marks
        box._init_(self,"Raj",23)


obj2=box2(23)
print(obj2.marks)
print(obj2.nameOfStudent)
print(obj2.rollNo)
