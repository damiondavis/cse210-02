from hilo import Hilo
"""
This section of code will have the bulk of the hilo game code in it. It will take the user input, pick the random card, update the score, 
and control the output of the score.
"""
class Director:

  def __init__(self):
    # We want to create a new instance of the game here and assign the Hilo class to a variable - Jordan
    
    self.cards = []
    self.is_playing = True
    self.score = 0
    self.total_score = 0

    # Here we assign the Hilo class to a variable and I believe this is
    # how we would go about running it to generate the first card, not sure though. - Jordan
    hilo = Hilo()

  def start_game(self):

    while self.is_playing:
      self.get_inputs()
      self.do_updates()
      self.do_outputs()


  def get_inputs(self):
    # this function allows us to ask the user if they would like to play
    # and if they say yes then we initiate the draw function from the hilo file.
    # after which we want to ask the user to guess a number and compare that
    # to the self.value integer generated via hilo.draw. - Jordan
    draw_cards = input("Would you like to play? [y/n] ")
    self.is_playing = (draw_cards == "y")
    # Here we assign the random card value to a variable/ attribute and ask the player to guess higher or lower - Jordan
    card_value = Hilo.draw(self)
    print(f"The first card's number is {card_value}")
    guess = input("would you like to guess the next to be higher or lower? [h/l] ")



  def do_updates(self):
    if not self.is_playing:
      return



  def do_outputs(self):
    if not self.is_playing:
      return
