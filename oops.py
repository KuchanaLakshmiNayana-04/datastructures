
#inheritance
#single inheritance
class Parent:
    def land(self):
        print("i have 10 acers of land")
class child:
    def child(parent):
        pass
obj = child()
obj=Parent()
obj.land()

#multi inheritance

class Parent1:
    def land(self):
        print("i have 10 acers of land")
class Parent2:
    def gold(self):
        print("i have 10 kgs of GOLD")
class child(Parent1,Parent2):
        pass
obj = child()
obj.land()
obj.gold()
#multi level inheritance

class grandParent:
    def land(self):
        print("i have 10 acers of land")
class Parent(grandParent):
    def gold(land):
        print("i have 10 kgs of GOLD")
class child(Parent):
        pass
obj = child()
obj.land()
obj.gold()

#hirearchial
class grandParent:
    def land(self):
        print("i have 10 acers of land")
class Parent(grandParent):
    def gold(land):
        print("i have 10 kgs of GOLD")
class child(Parent):
        pass
obj = child()
obj.land()
obj.gold()

#hybrid
class grandParent:
    def land(self):
        print("i have 10 acers of land")
class Parent(grandParent):
    def gold(land):
        print("i have 10 kgs of GOLD")
class child(Parent,grandParent):
        pass
obj = child()
obj.land()
obj.gold()


#polymorphism


class A:
    def a(self):
        print("welcome")
class B(A):
    def a(self):
        print("good byee")
class C(B):
    def a(self):
        print("get lost")
obj=C()
obj.a()



#Encapsulation
#two types 1,attribute 2,method 
#attribute method
class Bank:
    def __admin(self):
        print("amount is:",1000)
obj = Bank()
#obj.admin() # error because it is private
obj._Bank__admin()#output because NAME MANGLING


#abstractmethod
from abc import ABC, abstractmethod
class Bike (ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def acc(self):
        pass
class Bullet(Bike):
    def engine(self):
        print("it has 1000cc of engine")
    def acc(self):
        print("it can pickup in 1.2 sec")
gt = Bullet()
gt.engine()




