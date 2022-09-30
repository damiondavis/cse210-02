import random
"""
To create the deck of cards the player will be drawing from and to calculae the points.
"""
class Hilo:
  
  def __int__(self):
    # self.correct is to keep track if the users input is correct or not and will be changed in another file
    self.correct = True
    # needed to create the variable so that we can have the variable have a random number inserted into it
    self.value = 0
    # set the points as zero even though they will start with 300 points so that the portion of code will be in another file
    self.points = 0
   
  def draw(self):
    
    # If I understand random.randint correctly this will randomly choose a number between 1 and 13
    self.value = random.randint(1, 13)
    # I am not sure if the score system will work yet. I am questioning the else statment because it is negative, but I hope it works
    # I updated this statement so that it functions properly (I think), we don't need an if not statement here - Jordan
    if self.correct:
      self.points = 100 
    else:
       self.points = -75