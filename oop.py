
#class in python
class unidept :

    #all parameter are set in initial stage 
    # def __init__ (self,c,d):
    #      self.a=c
    #      self.b=d
   
    def __init__(self) -> None:
        pass


    def eee(self):
        print("eee")

    def cse(self):
        print("cse")
    
    def civil(self):
        print("civil")

    def sum(self,a,b): 
       return a+b 

#object create
u=unidept()

u.civil()
u.cse()
u.civil()
print(u.sum(10,20))