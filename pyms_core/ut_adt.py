from  adt import *

class A(Adt):
    Schema = (('A_i', int), ('A_s', str))
    
#    def __init__(self):
#        Adt.__init__(self)
    
class B(A):
    Schema = (('B_i', int), ('B_s', str))
    
#    def __init__(self):
#        A.__init__(self)
    
class C(Adt):
    Schema = (('C_i', int), ('C_AA', A))
    
class D(A,C):
    Schema = (('D_i', int),)
 
a = C()
a.C_AA = B()
#b = B()
#c = C()
#d = D()


#print (a.get_shema())
##print (a.__class__)
parser = ShemaParser(type(a))

for c in parser.Classes:
    print (c.__name__)

print("***")
for at in parser.Attributes:
    print (at)
    
print("***")
for n in parser.Names:
    print (n)

#print("***")
#for t in parser.Types:
#    print (t)
#    
#for n in parser.names():
#    print(n)
#    
#print('***')
#for t in parser.types():
#    print(t)
#    
#    
#print('***')
#for a in parser.elements():
#    print(a, type(a))
##print (b.get_shema())
##print (c.get_shema())
##print (d.get_shema())
#
#for t,x in parser.Attributes:
#    print(t, x)
#   
print ("****") 
print(a.__dict__)
