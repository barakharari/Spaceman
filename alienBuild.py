from tkinter import *

class AlienBuild:
  
  def __init__(self, canvas):
    
    self.__alienRight = PhotoImage(file = "alienRight.gif")
    self.__alienLeft = PhotoImage(file = "alienLeft.gif")
    self.__directionStatus = ""
    self.__canvas = canvas

  def createAlien(self):
    self.__alien = self.__canvas.create_image(50, 200, \
                  image = self.__alienRight, tag = "alien")
    return self.__alien

  def getRightImage(self):
    return self.__alienRight

  def getLeftImage(self):
    return self.__alienLeft

  def handleAlienMovement(self):
    if (self.__directionStatus == "right"):
      self.__canvas.move("alien", 7, 0)      
      if self.__canvas.coords("alien")[0] >= 475:
        self.__directionStatus = "left"       
    elif (self.__directionStatus == "left"):
      self.__canvas.move("alien", -7, 0)
      if self.__canvas.coords("alien")[0] <= 25:
        self.__directionStatus = "right"       
    elif (self.__directionStatus == "up"):
      self.__canvas.move("alien", 0, -7)    
      if self.__canvas.coords("alien")[1] <= 25:
        self.__directionStatus = "down"       
    elif (self.__directionStatus == "down"):
      self.__canvas.move("alien", 0, 7)     
      if self.__canvas.coords("alien")[1] >= 475:
        self.__directionStatus = "up"

  def touches(self, window):
  # Creating the controls and tying them to the functions
    window.bind('<Up>', self.__changeImageUp)
    window.bind('<Down>', self.__changeImageDown)
    window.bind('<Right>', self.__changeImageRight)
    window.bind('<Left>', self.__changeImageLeft)

  def __changeImageUp(self, event):
    if self.__directionStatus == "right":
      self.__canvas.itemconfig(self.__alien, image = self.__alienRight)
    else:
      self.__canvas.itemconfig(self.__alien, image = self.__alienLeft)
    self.__directionStatus = "up"
  def __changeImageDown(self, event):
    if self.__directionStatus == "right":
      self.__canvas.itemconfig(self.__alien, image = self.__alienRight)
    else:
      self.__canvas.itemconfig(self.__alien, image = self.__alienLeft)
    self.__directionStatus = "down"
  def __changeImageLeft(self, event):
    self.__canvas.itemconfig(self.__alien, image = self.__alienLeft)
    self.__directionStatus = "left"
  def __changeImageRight(self, event):
    self.__canvas.itemconfig(self.__alien, image = self.__alienRight)
    self.__directionStatus = "right"


    
