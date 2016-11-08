'''
Fizz Buzz
'''
three = False
five = False

x =0
while x <16:
    x += 1
    three = False
    five = False
    
    if x%3 == 0:
        three = True
    
    if x%5 == 0:
        five = True 
    
    if three and five:
        print "Fizz Buzz"
    elif three:
        print "Fizz"    
    elif five:
        print "Buzz"
    else:
        print x
        