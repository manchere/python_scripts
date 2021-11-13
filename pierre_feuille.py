import maya.cmds as cmds
import random

def aug(axe):
    return -random.uniform(-0.2,02) if axe < 0 else random.uniform(-0.2,0.2)

def caillou():
    cmds.polySphere(sx=20,sy=20)
    nb = cmds.polyEvaluate(v=True)
    for i in range(0,nb,5):
        cmds.softSelect(sse=True, ssd=1.5)
        pos = "pSphere1.vtx["+str(i)+"]"
        cmds.select(pos)
        cmds.move(aug(pos[0]), aug(pos[2]), xz=True, r=True)
        cmds.move(aug(pos[0]), aug(pos[2]), xz=True, r=True)
        cmds.softSelect(sse=False)

def feuille():
    cmds.polyTorus(r=3)
    nbf = cmds.polyEvaluate(v=True)
    for i in range(0, nbf,3):
        f= cmds.polyCube(sx=2, sy=2, w=0.3, h=0.05, d=0.3)
        pos = cmds.xform("pTorus1.vtx["+str(i)+"]", query=True, ws=True, t=True)
        cmds.select(f)
        cmds.move(pos[0], pos[1], pos[2])

def sciseaux():
    cmds.polyTorus()
    for i in range(0, cmds.polyEvaluate(face=True), 2):
        cmds.polyDelFacet("pTorus1.f["+str(i)+"]")

caillou()
feuille()
sciseaux()
