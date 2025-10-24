class A:
    def hablar(self):
        print("Hola desde A")
    
class B(A):
    pass
    # def hablar(self):
    #     print("Hola desde B")
            
class C(A):
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):
    pass
    # def hablar(self):
    #     print("Hola desde D")
        
d = D()

d.hablar()