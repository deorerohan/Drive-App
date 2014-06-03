#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()

if "setting" not in form:
    print "<h1>The box was not checked</h1>"
else:
    text=form["setting"].value
    print "<h1>The check box was ticked:</h1>"
    print text
