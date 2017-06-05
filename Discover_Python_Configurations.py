import sys
import nltk
import sklearn

print ("Configurations")
print (sys.version) + str("\n")
print str(sys.version_info) + str("\n")
print (sys.path)

print('The nltk version is {}.'.format(nltk.__version__))
print('The scikit-learn version is {}.'.format(sklearn.__version__))
