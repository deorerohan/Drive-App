def returntext():
	return "this is my test"

d1 = "device 1"
d2 = "device 2"
devices = {d1:2,d2:3}



def getdevices():
	return devices.keys()

	
def addcheckbox(name):
    print "<input type=\"checkbox\" value=\""+name+"\" value=\"set\">" +name+ "<br>"
