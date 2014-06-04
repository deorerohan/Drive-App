def returntext():
	return "this is my test"

d1 = "device 1"
d2 = "device 2"
devices = {d1:2,d2:3}



def getdevices():
	return devices.keys()

	
def addcheckbox(name, ischecked):
    if ischecked:
        print "<input type=\"checkbox\" name=\""+name+"\" value=\"set\" checked>" +name+ "<br>"
    else:
         print "<input type=\"checkbox\" name=\""+name+"\" value=\"set\">" +name+ "<br>"
        
