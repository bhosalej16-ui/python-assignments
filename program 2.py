class person :
    def __init__ (self,height,weight,age):
        self.height=height
        self.weight=weight
        self.age=age

    def display(self):    
        print(self.height,self.weightself.age)

class student(person):
    def __init__ (self,height,weight,age,name,marks):
        person.__init__(self,height,weight,age)
        self.marks=marks        
        self.name=name

    def write(self):
        print(self.height,self.weight,self.age,self.name,self.marks)
   
    def stud(self):
        print("I am Student")

T=student("13'33","66 kg","21","Aryan","90")
T.display()
T.write()
T.stud()
T.marks=99
T.write()      