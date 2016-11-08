fiboSeq =[]

a,b = 7,8
counter =1
print str(counter) + " " +str(a)
print str(counter) + " " +str(b)
while (counter<11):
    fiboSeq.append(a)
    a,b=b,a+b
    print str(counter) + " " + str(b)
    counter += 1

print fiboSeq

'''
1.	Choose two smallish numbers (less than 10)
2.	Add the two numbers and write the results on the third line
3.	Add the second and third line to make the fourth
4.	Repeat until you have ten lines
5.	Take the 7th number and multiply it by 11
'''