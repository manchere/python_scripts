import maya.cmds as cmds
import functools

def generateUI(pWindowTitle, pcallBack):

    windowID = 'myWindowID'

    if cmds.window(windowID, exists =True):
        
        cmds.deleteUI(windowID)

    cmds.window(windowID,title=pWindowTitle,sizeable=False,resizeToFitChildren= True)

    cmds.rowColumnLayout(numberColumn = 3,columnWidth=[(1,75),(2,60),(3,60)],columnOffset=[1,'right',3])

#when interface element is created is placed in the next available position in the current layout
    cmds.text(label='Time Range:')

    startTimeField = cmds.inField(value=cmds.playbackOptions(q=True,minTime=True))

    endTimeField = cmds.inField(value=cmds.playbackOptions(q=True,maxTime=True))

    cmds.text(label='Attribute')

    targetAttributeField = cmds.textField(text='rotateY')

    cmds.separator(h=10,style='none')

    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')

    cmds.separator(h=10,style='none')

    cmds.button(label='Apply',command = functools.partial(pcallBack,
                                        startTimeField,
                                        endTimeField,
                                        targetAttributeField,*pArgs) )

def cancelCallBack(*pArgs):
    if cmds.window(windowID, exists=True):
            cmds.deleteUI(windowID)
    cmds.button(label='Cancel',command=cancelCallback)
    
    cmds.showWindow()

def applyCallBack(*pArgs,pstartTimeField,pendTimeField,ptargetAttribute):

    print 'Apply button pressed'

    startTimeField = cmds.inField(value=cmds.playbackOptions(q=True, minTime=True))
    endTimeField = cmds.inField(value=cmds.playbackOptions(q=True, maxTime=True))


    creatUI('My title',applyCallBack)






