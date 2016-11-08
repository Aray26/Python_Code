'''
Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.

group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]
'''
import sys

print "What are the elements you want to cut up?"
x = raw_input().split(' ')

print "How big are the chunks ?"
y = int(raw_input())
i = 0
final_list = []

chunk_size_counter = 0

for i in x:
    print "i is " + str(i)
    print "chunk_size_counter is " + str(chunk_size_counter)
    print "y is " + str(y)

    if chunk_size_counter < y:
        final_list.append(i)
        chunk_size_counter += 1
        print "if i is " + str(i)
        print "if chunk_size_counter is " + str(chunk_size_counter)
        print "if y is " + str(y)

        if (i is x[-1]):
            print "last i is " + str(i)
            print "last chunk_size_counter is " + str(chunk_size_counter)
            print "last y is " + str(y)

            print "last element is " + str(i)
            print final_list
    else:
        print "final_list is " + str(final_list) + "\n"
        final_list = []
        chunk_size_counter = 0
        print "i is now " + str(i)
        print "chunk_size_counter is  now " + str(chunk_size_counter)
        print "y is now " + str(y)
'''
final_list = []

for i in elements:
   print "i is " + str(i)
   count=0
   if count < y:
      print count
      count +=1
      counter +=1
      final_list.append(i)
   print "chunk #" + str(counter) + " is " + str(final_list)
   final_list = []
   count=0
   
#   print "final chunk " + str(final_list)
    
'''
