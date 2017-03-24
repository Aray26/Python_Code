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

