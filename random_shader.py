import maya.cmds as cmds
import random as rnd
cScheme = {
    'yellow': [255,255,0],
    'blue': [0,0,255],
    'red': [255, 0, 0],
    'purple': [255,0,255],
    'green': [0, 255, 0]
}

mScheme = ['standardSurface', 'rampShader', 'lambert', 'blinn', 'phong', 'anisotropic', 'phongE']

class Shader:
    def create_shader(self, node_type= 'blinn'):
        mtl = cmds.shadingNode(node_type, asShader=True)
        sg = cmds.sets(name="%sSG" % node_type, empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr("%s.outColor" % mtl, "%s.surfaceShader" % sg)
        return mtl, sg

    def set_color(self, key_color, shader_colors, shaderFunc):
        meshes = cmds.ls(selection=True, dag=True, type="mesh", noIntermediate=True)
        material, sgrp = shaderFunc
        cmds.setAttr(material + ".color", shader_colors[key_color][0], shader_colors[key_color][1], shader_colors[key_color][2], type='double3')
        cmds.sets(meshes, forceElement=sgrp)

class UI:
    def __init__(self, name):
        self.Window = name

        if cmds.window(self.Window, exists=True, w=350):
            cmds.deleteUI(self.Window, window=True)

        my_win = cmds.window(title=self.Window)
        cmds.columnLayout(adjustableColumn=True)
        cmds.showWindow(my_win)

    def make_btn(self):
        cmds.button(l='Random', command='random()')

def random():
    r = rnd.randint(0, 6)

    shaderFunc = shader.create_shader(mScheme[r])
    rndcol = rnd.choice(list(cScheme.keys()))

    shader.set_color(rndcol, cScheme, shaderFunc)

shader = Shader()
ui = UI('Shaders')
ui.make_btn()
