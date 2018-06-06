#!/usr/bin/python
v0= input("Ievadiet sākotnējo bumbas ātrumu: ")
t= input("Ievadiet bumbas kustības laiku: ")
g=9.81

y=(v0*t)-(g*(t**2)/2)
print "Pēc "+ str(t) +" sekundēm bumba būs "+str(y)+" metri virs zemes."

