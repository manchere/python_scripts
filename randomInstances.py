#randomnInstances.py

import maya.cmds as cmds
import random as rnd

rnd.seed(1234)

results = cmds.ls(orderedSelection=True)

print 'result: %s' % (result) 

transformName = results[0]

instanceGrpName = cmds.group(empty = True, name = transformName+'_instancegrp#') 

for i in range(0,50):

	instanceResult = cmds.instance(transformName, name = transformName + '_instance#')
	
	cmds.parent(instanceResult, instanceGrpName)

	#print 'instanceResult ' + str( instanceResult )
	
	#translation of polyCubes
	x = rnd.uniform(0 , -10)
	y = rnd.uniform(0, 10)
	z = rnd.uniform(-34, 20)
	
	cmds.move(x,y,z,instanceResult)
	
	
	#rotation of polyCubes
	xr = x = rnd.uniform(0 , 360)
	yr = rnd.uniform(0, 360)
	zr = rnd.uniform(180, -180)
	
	cmds.rotate(xr,yr,zr,instanceResult)
	
	scaling  = rnd.uniform(0.4, 1.4)
	
	cmds.scale(scaling, scaling, scaling, instanceResult)
	
cmds.hide(transformName)
	
cmds.xform(instanceGrpName,centerPivots= True)
	