#multiple inheritance(it creates Diamond problem in java)
#it has more than one parent class

class multipleinheritance:
    def msg(self):
        print("class A")
class B:
    def msg(self):
        print("class B")
class C(multipleinheritance,B):
    def msg(self):
        print("class c")
Multipleinheritance=multipleinheritance()
Multipleinheritance.msg()
b=B()
b.msg()
c=C()
c.msg()
    
