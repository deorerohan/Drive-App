# main file containing everything to start with
import mygpio


devices = {'bed light': 2, 'bed fan': 3}

# avilable pins 3-5-7-8-10-11-12-13-15-16-18-18-19-21-22-23-24-26

# basic application will do following
mygpio.start()
mygpio.setuppin(7, True)
mygpio.stop()


# this file will hold all pin and there respective type/name
# pins will be represented as bedlight, hallfan, tv, etc.
