#keyRotation.py

import maya.cmds as cmds

def keyFullRotation(pObjectName, pStartTime, pEndTime, pTargetAttribute):
	
	#objectTypeResult = cmds.objectType(objectName)
		
	cmds.cutKey(pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute)
	cmds.setKeyframe(pObjectName,time=pStartTime,attribute= pTargetAttribute, value=0)
	cmds.setKeyframe(pObjectName,time=pEndTime,attribute= pTargetAttribute, value=360)

selectionList = cmds.ls(selection = True, type='transform')

if len(selectionList) >= 1:
	
	startTime = cmds.playbackOptions(query = True, minTime=True)
	endTime = cmds.playbackOptions(query = True, maxTime=True)

	print 'Selected items %s' % (selectionList) 
	
	for objectName in selectionList:
		
		keyFullRotation(objectName, startTime, endTime,'rotateY')
 
	
else:
	
	print 'Please select at least one object'
	
	
