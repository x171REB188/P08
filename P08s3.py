#!/usr/bin/python
v0=20
t=18
g=9.81

#loops
for t in range(1, 20):
    y=(v0*t)-(g*(t**2)/2)
    print "Pēc "+ str(t) +" sekundēm bumba būs "+str(y)+" metri virs zemes."

# izvade
from numpy import linspace,array
x=linspace(0,1,19)   
y=(v0*t)-(g*(x**2)/2)

from matplotlib import pyplot as p
p.plot(x,y,color="#ff0000", label="super")
p.legend()
p.show()
