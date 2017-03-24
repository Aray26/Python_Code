from __future__ import print_function

print("%10.3E"% (356.08977))


s = "Price: $ %17.8f"% (356.08977)
print(s)
#Price: $   356.09


s = "Price: $ %17s"% ("tiger")
print(s)

s = "Price: $ %17d"% (356.98977)
print(s)

x = 378
print("The value is {:08d}".format(x))
#The value is 000378
x = -378
print("The value is {:08d}".format(x))
#The value is -00378

print("The value is {:,}".format(x))
#The value is 78,962,324,245
print("The value is {0:6,d}".format(x))
#The value is 5,897,653,423
x = 5897653423.89676
print("The value is {0:12,.3f}".format(x))
#The value is 5,897,653,423.897

print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))

print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))

data = dict(province="Ontario",capital="Toronto")
print (data)
print("The capital of {province} is {capital}".format(**data))
#The capital of Ontario is Toronto

print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))

print ("++++++++++++++++++++++++++++++++++++++\n")

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string.format(**capital_country))
    
#Other string methods for Formatting
#The string class contains further methods, which can be used for formatting purposes as well: ljust, rjust, center and zfill

#Let S be a string, the 4 methods are defined like this:
'''
S.center(width[, fillchar]) -> str

    Return S centred in a string of length width. Padding is done using the specified fill character. The default value is a space.

    Examples:

    >>> s = "Python"
    >>> s.center(10)
    '  Python  '
    >>> s.center(10,"*")
    '**Python**'

    ljust(...):

     S.ljust(width[, fillchar]) -> str 

    Return S left-justified in a string of length "width". Padding is done using the specified fill character. If none is given, a space will be used as default.

    Examples:

    >>> s = "Training"
    >>> s.ljust(12)
    'Training    '
    >>> s.ljust(12,":")
    'Training::::'
    >>> 

    rjust(...):

    S.rjust(width[, fillchar]) -> str

    Return S right-justified in a string of length width. Padding is done using the specified fill character. The default value is again a space.

    Examples:

    >>> s = "Programming"
    >>> s.rjust(15)
    '    Programming'
    >>> s.rjust(15, "~")
    '~~~~Programming'
    >>> 

    zfill(...):

     
    S.zfill(width) -> str

    Pad a string S with zeros on the left, to fill a field of the specified width. The string S is never truncated. This method can be easily emulated with rjust.

    Examples:

    >>> account_number = "43447879"
    >>> account_number.zfill(12)
    '000043447879'
    >>> # can be emulated with rjust:
    ... 
    >>> account_number.rjust(12,"0")
    '000043447879'
    >>> 
'''
print "close this file"


