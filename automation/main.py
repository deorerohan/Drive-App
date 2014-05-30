# main file containing everything to start with
import mygpio

# basic application will do following
mygpio.start()
mygpio.setuppin(7, True)
mygpio.stop()


# this file will hold all pin and there respective type/name
# pins will be represented as bedlight, hallfan, tv, etc.
