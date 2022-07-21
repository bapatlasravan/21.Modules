"""
import Mathemetical_operations
x=10
y=20
z=Mathemetical_operations.add(x,y)
print(z)
"""

#importing only one operation from mathemetical_operation
"""
from Mathemetical_operations import multi
x=10
y=20
z=multi(x,y)   #Here we use only multi operation if we give add then we get an error
print(z)
"""
#IF we want all opertions with above syntax we use *
"""
from Mathemetical_operations import *
x=10
y=20
z=div(x,y)  
print(z)
"""


# we can also give alias name for modules
"""
import Mathemetical_operations as calci
x=10
y=20
z=calci.add(x,y)
print(z)
"""

#One of the inbuilt module in pythone was platform
"""
import platform
print(platform.system())  #windows
"""