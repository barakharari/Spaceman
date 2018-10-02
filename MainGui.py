from tkinter import *
from alienBuild import *
from rockBuild import *
import tkinter.messagebox
import random

class GameGUI:

  TIME = 60
  
  def __init__(self):
    # Create the main GUI window
    self.__mainWindow = Tk()
    # Creating the canvas

    self.__canvas = Canvas(self.__mainWindow, width = 500, height = 500)
    self.__canvas.pack()

    self.__time = GameGUI.TIME
    # Images and adjustments
    
    self.__backgroundImage = PhotoImage(file = "spaceBackground.gif")
    self.__background = self.__backgroundImage.zoom(5,5)

    # Initialize score
    self.__score = 0
    self.__scoreUpdate = StringVar()
    self.__scoreUpdate.set(value = self.__score)
    
    self.__scoreText = Label(self.__mainWindow, text = "Score: ", \
        font = ('Time bold', 20), foreground = "white", background = "black")
    self.__canvas.create_window(55, 25, window = self.__scoreText)
    
    self.__scoreLabel = Label(self.__mainWindow, textvariable = self.__scoreUpdate,\
        font = ('Time bold', 20), foreground = "white", background = "black")
    self.__canvas.create_window(100, 25, window = self.__scoreLabel)

    self.__timeLabelVar = StringVar()
    self.__timeLabelVar.set(value = self.__time)

    self.__timeLeftText = Label(self.__mainWindow, text = "Time Left: ", \
        font = ('Time bold', 20), foreground = "white", background = "black")
    self.__canvas.create_window(380, 25, window = self.__timeLeftText)
    
    self.__newTimeLabel = Label(self.__mainWindow, textvariable = \
        self.__timeLabelVar, font=('Time bold', 20), fg = "white", bg = "black")
    self.__canvas.create_window(450, 25, window = self.__newTimeLabel)


    self.__inGame = "In Game"
    # Initialize direction status
    self.directionStatus = ""

    
    # Put create alien and background
    self.__alien = AlienBuild(self.__canvas)
    self.__alien.createAlien()
    self.__alien.touches(self.__mainWindow)
    
    self.__canvas.create_image(0, 0, image = self.__background)
    self.__canvas.tag_lower(self.__background)

    # Create rocks for pick up
    self.__rock = RockBuild(500, 500)
    self.__rock.createRock(self.__canvas)
      

    self.__playButton = Button(self.__mainWindow, text = "Play",\
                               command = self.start)
    self.__canvas.create_window(250, 350, window = self.__playButton)

    self.__quitButton = Button(self.__mainWindow, text = "Quit",\
                               command = self.closeWindow)
    self.__canvas.create_window(250, 300, window = self.__quitButton)


    self.__mainWindow.mainloop()

# Handles all object movement since built on a timer

  def move(self):
    if self.__inGame == "In Game":
      self.__alien.handleAlienMovement()

      # Layering
      self.__canvas.tag_raise("alien")

      # Checking if you touched a rock
      self.touchRock()
  
      self.__canvas.after(40, self.move)

  def touchRock(self):
    alienCoordinates = self.__canvas.coords("alien")
    alienLocationX = alienCoordinates[0]
    alienLocationY = alienCoordinates[1]

    rockCoordinates = self.__canvas.coords("rock")
    rockLocationX = rockCoordinates[0]
    rockLocationY = rockCoordinates[1]
    
    differenceX = alienLocationX - rockLocationX
    differenceY = alienLocationY - rockLocationY

    if (abs(differenceX) > -50 and abs(differenceX) < 50):
      if (abs(differenceY) > -50 and abs(differenceY) < 50):
        moveX = 200
        moveY = 200
        while rockLocationX + moveX > 500\
               or rockLocationX + moveX < 0\
               or rockLocationY + moveY > 500\
               or rockLocationY + moveY < 40:
          moveX = random.randrange(-500, 500)
          moveY = random.randrange(-500, 500)
        self.__canvas.move("rock", moveX, moveY)
        self.incrementScore()

  def incrementScore(self):
    self.__score += 1
    self.__scoreUpdate.set(self.__score)

  def startTimer(self):
    if self.__time > 0:
      self.__time -= 1
      self.__timeLabelVar.set(value = self.__time)
      self.__canvas.after(1000, self.startTimer)
    else:
      self.end()

  def start(self):
    self.__inGame = "In Game"
    self.__score = 0
    self.__scoreUpdate.set(self.__score)
    self.move()
    self.startTimer()
    self.time = GameGUI.TIME
    self.__playButton.destroy()
    self.__quitButton.destroy()

  def end(self):
    self.__inGame = "Game Over"
    tkinter.messagebox.showinfo("Result","Your score is: %s" % self.__score)
    self.reset()

  def reset(self):
    self.__time = GameGUI.TIME
    self.__playButton = Button(self.__mainWindow, text = "Play",\
                               command = self.start)
    self.__canvas.create_window(250, 350, window = self.__playButton)
    self.__quitButton = Button(self.__mainWindow, text = "Quit",\
                               command = self.closeWindow)
    self.__canvas.create_window(250, 300, window = self.__quitButton)

  def closeWindow(self):
    self.__mainWindow.destroy()
      
GameGUI()
