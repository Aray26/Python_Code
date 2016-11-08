total = 0
final_total = 0
final_depth_level = 10
current_depth = 1

print "Gimme a number less than 10 "
#x = int(raw_input('> '))
x=8

print "Gimme another number less than 10 "
#y = int(raw_input('> '))
y=9


def recursion_depth(depth):
    if (current_depth == 1):
        print "at depth of "+str(depth)
        total = x +y
        previous_total = y
        final_total = total
        current_depth += 1
    elif (current_depth >= final_depth_level):
        print "end depth " + str(depth)
        exit()
    else:
        print "Exiting"
        print "here"

def add_ten_times(g, h):
    print g
    print h
    result1 = g + h
    total = result1

def add_ten_times_1(g, h):
    print result1
    result2 = h + result1
    total += result2
    print result2
    result3 = result1 + result2
    total += result3
    print result3
    result4 = result3 + result2
    total += result4
    print result4
    result5 = result4 + result3
    total += result5
    print result5
    result6 = result5 + result4
    total += result6
    print result6
    result7 = result6 + result5
    total += result7
    print result7
    result8 = result7 + result6
    total += result8
    print result8
    result9 = result8 + result7
    total += result9
    print result9
    result10 = result9 + result8
    total += result10
    print result10

    print "total via addition " + str(total)
    total_7th_item_times_11 = int(result7)*11
    print "total via 7th item times 11 " + str(total_7th_item_times_11)

#for number_of_additions in range(1, 10):
add_ten_times(x,y)

recursion_depth(current_depth)