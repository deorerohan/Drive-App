#!/usr/bin/env python

import cgi
import cgitb
import test

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()

var1 = "setting"

if var1 not in form:
    print "<h1>The box was not checked</h1>"
    print test.returntext()
    devicelist = test.getdevices()
    print devicelist[0]
    print devicelist[1]

else:
    text=form[var1].value
    print "<h1>The check box was ticked:</h1>" 
	
#print "<form action=\"/cgi-bin/examples/checkbox.py\" method=\"POST\">"
    devices=test.getdevices()
    for item in devices:
		test.addcheckbox(item)
    print "<input type=\"submit\" value=\"Submit\" name=\"submit\">"  
	#print "</form>"
	
	
	
if request.POST.get('submit'):
	print "Submit was pressed"
else :
	print "Submit was not pressed"
