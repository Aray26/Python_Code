import sys

print sys.argv

x = sys.argv
 
y =  x[1::]

print list(y)
x=[]

for i in y:
    if i in x: 
       print "Already there"
    else:
       x.append(i)
        


print str(x)    