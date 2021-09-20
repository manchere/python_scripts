#keyRotation.py

import maya.cmds as cmds

selectionList = cmds.ls(selection = True, type='transform')

if len(selectionList) >= 1:
	
	startTime = cmds.playbackOptions(query = True, minTime=True)
	endTime = cmds.playbackOptions(query = True, maxTime=True)

	print 'Selected items %s' % (selectionList) 
	
	for objectName in selectionList:
 
		objectTypeResult = cmds.objectType(objectName)
		
		cmds.cutKey(objectName, time=(startTime, endTime), attribute='rotateY')
		cmds.setKeyframe(objectName,time=startTime,attribute= 'rotateY', value=0)
		cmds.setKeyframe(objectName,time=endTime,attribute= 'rotateY', value=360)
	
else:
	
	print 'Please select at least one object'