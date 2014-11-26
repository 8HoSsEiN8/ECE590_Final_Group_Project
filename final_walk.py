#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*

# ******************************************************

# Chris Glomb
# Final Project
# 11/25/14

# this code uses the hubo-simple-demo-python as the base

# ******************************************************

import ach
import time
import math
from ctypes import *
import dyno_include as di

d = ach.Channel(di.DYNO_REF_NAME)
d.flush()

# feed-back will now be refered to as "ref"
dyno = di.DYNO_REF()

dyno.LHR, dyno.LHP, dyno.LKP, dyno.LAP, dyno.CHR, dyno.CHP, dyno.CKP, dyno.CAP, dyno.RHR, dyno.RHP, dyno.RKP, dyno.RAP = 0,0,0,0,0,0,0,0,0,0,0,0

x = 0
y = 0
t = 0
i = 0
shift = 14

def toDyno():
	dyno.LHR = dyno.LHR
	dyno.LHP = dyno.LHP
	dyno.LKP = -dyno.LKP
	dyno.LAP = -dyno.LAP
	dyno.CHR = dyno.CHR
	dyno.CHP = dyno.CHP
	dyno.CKP = -dyno.CKP
	dyno.CAP = -dyno.CAP
	dyno.RHR = dyno.RHR
	dyno.RHP = dyno.RHP
	dyno.RKP = -dyno.RKP
	dyno.RAP = -dyno.RAP
	d.put(dyno)

# get in walking position
while i < 5:
	x += 0.1
	dyno.LHP = -x
        dyno.LKP = 2*x
        dyno.LAP = -x
        dyno.CHP = -x
        dyno.CKP = 2*x
        dyno.CAP = -x
        dyno.RHP = -x
        dyno.RKP = 2*x
        dyno.RAP = -x
	toDyno()
	#print x
	i += 1
	time.sleep(.2)

# raise up on center leg
i = 0
while i < 3:
	x = 0.12
	dyno.CHP = dyno.CHP + x
        dyno.CKP = dyno.CKP - 2*x
        dyno.CAP = dyno.CAP + x
	toDyno()
	i += 1
	time.sleep(.1)

time.sleep(.3)

# take first step forward with outer legs
i = 0
x = 0.03
while i < 6:
	# outer feet forward
	dyno.LHP = dyno.LHP - x
        dyno.LAP = dyno.LAP + x
	dyno.RHP = dyno.RHP - x
        dyno.RAP = dyno.RAP + x
        # center foot back
        dyno.CHP = dyno.CHP + x
        dyno.CAP = dyno.CAP - x
        # center leg down
        dyno.CHP = dyno.CHP - .06
        dyno.CKP = dyno.CKP + .12
        dyno.CAP = dyno.CAP - .06
        toDyno()
	i += 1
	time.sleep(.1)

# raise up on outer legs
i = 0
x = 0.12
while i < 3:
	dyno.LHP = dyno.LHP + x
        dyno.LKP = dyno.LKP - 2*x
        dyno.LAP = dyno.LAP + x
        dyno.RHP = dyno.RHP + x
        dyno.RKP = dyno.RKP - 2*x
        dyno.RAP = dyno.RAP + x
	toDyno()
	i += 1
	time.sleep(.1)

time.sleep(.3)
	
# take step forward with center leg
i = 0
x = 0.075
while i < 6:
	# outer feet back
	dyno.LHP = dyno.LHP + x
        dyno.LAP = dyno.LAP - x
        dyno.RHP = dyno.RHP + x
        dyno.RAP = dyno.RAP - x
        # center foot forward
        dyno.CHP = dyno.CHP - x
        dyno.CAP = dyno.CAP + x
        # outer legs down
        dyno.LHP = dyno.LHP - .06
        dyno.LKP = dyno.LKP + .12
        dyno.LAP = dyno.LAP - .06
        dyno.RHP = dyno.RHP - .06
        dyno.RKP = dyno.RKP + .12
        dyno.RAP = dyno.RAP - .06
        toDyno()
	i += 1
	time.sleep(.1)
	
# raise up on center leg
i = 0
x = 0.12
while i < 3:
	dyno.CHP = dyno.CHP + x
        dyno.CKP = dyno.CKP - 2*x
        dyno.CAP = dyno.CAP + x
	toDyno()
	i += 1
	time.sleep(.1)

time.sleep(.3)

# take step forward with outer legs
i = 0
x = 0.075
while i < 6:
	# outer feet forward
	dyno.LHP = dyno.LHP - x
        dyno.LAP = dyno.LAP + x
        dyno.RHP = dyno.RHP - x
        dyno.RAP = dyno.RAP + x
        # center foot back
        dyno.CHP = dyno.CHP + x
        dyno.CAP = dyno.CAP - x
        # center leg down
        dyno.CHP = dyno.CHP - .06
        dyno.CKP = dyno.CKP + .12
        dyno.CAP = dyno.CAP - .06
        toDyno()
	i += 1
	time.sleep(.1)

# raise up on outer legs
i = 0
x = 0.12
while i < 3:
	dyno.LHP = dyno.LHP + x
        dyno.LKP = dyno.LKP - 2*x
        dyno.LAP = dyno.LAP + x
        dyno.RHP = dyno.RHP + x
        dyno.RKP = dyno.RKP - 2*x
        dyno.RAP = dyno.RAP + x
	toDyno()
	#print x
	i += 1
	time.sleep(.1)

time.sleep(.3)
	
# take step forward with center leg
i = 0
x = 0.075
while i < 6:
	# outer feet back
	dyno.LHP = dyno.LHP + x
        dyno.LAP = dyno.LAP - x
        dyno.RHP = dyno.RHP + x
        dyno.RAP = dyno.RAP - x
        # center foot forward
        dyno.CHP = dyno.CHP - x
        dyno.CAP = dyno.CAP + x
        # outer legs down
        dyno.LHP = dyno.LHP - .06
        dyno.LKP = dyno.LKP + .12
        dyno.LAP = dyno.LAP - .06
        dyno.RHP = dyno.RHP - .06
        dyno.RKP = dyno.RKP + .12
        dyno.RAP = dyno.RAP - .06
        toDyno()
	i += 1
	time.sleep(.1)
	
# raise up on center leg
i = 0
x = 0.12
while i < 3:
	dyno.CHP = dyno.CHP + x
        dyno.CKP = dyno.CKP - 2*x
        dyno.CAP = dyno.CAP + x
	toDyno()
	i += 1
	time.sleep(.1)

time.sleep(.3)

# take step forward with left leg
i = 0
x = 0.075
while i < 6:
	# outer feet forward
	dyno.LHP = dyno.LHP - x
        dyno.LAP = dyno.LAP + x
        dyno.RHP = dyno.RHP - x
        dyno.RAP = dyno.RAP + x
        # center foot back
        dyno.CHP = dyno.CHP + x
        dyno.CAP = dyno.CAP - x
        # center leg down
        dyno.CHP = dyno.CHP - .06
        dyno.CKP = dyno.CKP + .12
        dyno.CAP = dyno.CAP - .06
        toDyno()
	i += 1
	time.sleep(.1)

# raise up on left leg
i = 0
x = 0.12
while i < 3:
	dyno.LHP = dyno.LHP + x
        dyno.LKP = dyno.LKP - 2*x
        dyno.LAP = dyno.LAP + x
        dyno.RHP = dyno.RHP + x
        dyno.RKP = dyno.RKP - 2*x
        dyno.RAP = dyno.RAP + x
	toDyno()
	i += 1
	time.sleep(.1)

time.sleep(.3)
	
# take step forward with outer legs
i = 0
x = 0.075
while i < 6:
	# outer feet back
	dyno.LHP = dyno.LHP + x
        dyno.LAP = dyno.LAP - x
        dyno.RHP = dyno.RHP + x
        dyno.RAP = dyno.RAP - x
        # center foot forward
        dyno.CHP = dyno.CHP - x
        dyno.CAP = dyno.CAP + x
        # outer legs down
        dyno.LHP = dyno.LHP - .06
        dyno.LKP = dyno.LKP + .12
        dyno.LAP = dyno.LAP - .06
        dyno.RHP = dyno.RHP - .06
        dyno.RKP = dyno.RKP + .12
        dyno.RAP = dyno.RAP - .06
        toDyno()
	i += 1
	time.sleep(.1)

i = 0
x = 0.3
# stand back up
while i < 5:
	dyno.LHP = dyno.LHP + x
        dyno.LKP = dyno.LKP - 2*x
        dyno.LAP = dyno.LAP + x
        dyno.CHP = dyno.CHP + x
        dyno.CKP = dyno.CKP - 2*x
        dyno.CAP = dyno.CAP + x
        dyno.RHP = dyno.RHP + x
        dyno.RKP = dyno.RKP - 2*x
        dyno.RAP = dyno.RAP + x
	toDyno()
	i += 1
	time.sleep(.2)	

# Close the connection to the channels
d.close()









