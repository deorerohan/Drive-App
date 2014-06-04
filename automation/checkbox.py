#!/usr/bin/env python

import cgi
import cgitb
import test

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()

devices = test.getdevices()
print "<form action=\"/cgi-bin/examples/checkbox.py\" method=\"POST\">"

for dev in devices:

    if dev not in form:
        print dev + " is not checked"
        test.addcheckbox(dev, False)

    else:
        print dev + " is checked"
	test.addcheckbox(dev, True)
        


print "<input type=\"submit\" value=\"Submit\" name=\"submit\">"  
print "</form>"
	
	
#if request.POST.get('submit'):
#	print "Submit was pressed"
#else :
#	print "Submit was not pressed"
