#load Panda3D game system
import direct.directbase.DirectStart
from pandac.PandaModules import *

#load the model
model = loader.loadModel("3D model.egg")

#add model to 3D world
model.reparentTo(render)

#game start
run()