from tkinter import *
import random

class RockBuild:

  def __init__(self, canvasWidth, canvasHeight):
    self.__rockImage = PhotoImage(file = "SpaceRock.gif")
    self.__canvasWidth = canvasWidth
    self.__canvasHeight = canvasHeight

  def returnRock(self):
    return self.__rockImage

  def createRock(self, canvas):
    canvas.create_image(250, 400,\
                       image = self.__rockImage, tag = "rock")
    canvas.tag_raise(self.__rockImage)

