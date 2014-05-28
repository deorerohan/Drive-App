import two # importing from two.py file name without .py is its module name
import more.three

two.MyPrint('this is awesome') # calling function from two
more.three.MyThreePrint() # third module from diffrerent directory called.
print 'back to one.py' # to confirm that we are back to one.py
