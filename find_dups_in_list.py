import sys

print sys.argv

x = sys.argv
 
y =  x[1::]

print list(y)
x=[]
z = []

for i in y:
    if i in x:
       print "found dup"
       z.append(i)
    else:
       x.append(i)


print str(z)    