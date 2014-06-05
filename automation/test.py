import mygpio

d1 = "device 1"
d2 = "device 2"
devices = {d1:3, d2:5}
#available pins 3-5-7-8-10-11-12-13-15-16-18-18-19-21-22-23-24-26
InitGPIO = False

def returntext():
	return "this is my test"

def getdevices():
	if InitGPIO == False:
		InitGPIO = True
		mygpio.start()
		for dev in devices:
			mygpio.setuppin(devices.value, True)
	return devices.keys()

	
def addcheckbox(name, ischecked):
    if ischecked:
	mygpio.toggleswitch(devices[name], True)
        print "<input type=\"checkbox\" name=\""+name+"\" value=\"set\" checked>" +name+ "<br>"
    else:
	mygpio.toggleswitch(devices[name], False)
        print "<input type=\"checkbox\" name=\""+name+"\" value=\"set\">" +name+ "<br>"
        
