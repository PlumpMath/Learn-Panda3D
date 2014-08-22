#load Panda3D game system
import direct.directbase.DirectStart
from direct.showbase import DirectObject #add the keyboard or mouse function
from pandac.PandaModules import *

#make a class named "KeyboardManager" to process key presses
class KeyboardManager(DirectObject.DirectObject):
	def __init__(self):
		self.accept('a',self.fire)
	def fire(self):
		KeyboardManager.show()
		taskMgr.doMethodLater(0.05, KeyboardManager.hide, 'show')
		gunshot.play()
	@staticmethod
	def show():
		muzzleflash.show()
		muzzleflash2.show()
		light.setColor(VBase4(8.0, 8.0, 8.0, 1.0))
	@staticmethod
	def hide(t):
		muzzleflash.hide()
		muzzleflash2.hide()
		light.setColor(VBase4(0.5, 0.5, 0.5, 1.0))

#create an instance of "KeyboardManager"
KeyboardManager()

#disable "looking around"
base.disableMouse()

#load the gun sound
gunshot = base.loader.loadSfx("Gun_Shot.wav")

#load the gun 3D model
model = loader.loadModel("ak47.egg")

#find the muzzle flash (fire) in the 3D model
muzzleflash = model.find("**/muzzleflash")
muzzleflash2 = model.find("**/muzzleflash2")

#hide the muzzle flash when gun is off
muzzleflash.hide()
muzzleflash2.hide()

#add gun 3D model to "render" (render = 3D world)
model.reparentTo(render)

#position the camera correctly
camera.setPos(3.0, 5.0, 1.5)

#rotate the camera correctly
camera.setH(160)

#create a light
light = PointLight('light')

#set the light to be very dark
light.setColor(VBase4(0.5, 0.5, 0.5, 1.0))

#add the light to the camera
light_file = camera.attachNewNode(light)

#enable lighting for "render" (render = 3D world)
render.setLight(light_file)

#game start
run()