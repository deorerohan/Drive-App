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
    print text

    devices=test.getdevices()
    print "<input type=\"submit\" value=\""+devices[0]+"\"><br><input type=\"submit\" value=\"", devices[1]+"\">"


def addcheckbox(name):
    print "<input type=\"checkbox\" value=\""+name+"\""
