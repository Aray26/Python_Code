import sys

print sys.argv

x = sys.argv
 
y =  x[1::]

print list(y)
x=0

for i in y:
    x = int(i) * int(x) 


print str(x)    