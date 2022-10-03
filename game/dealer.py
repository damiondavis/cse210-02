from game.hilo import Hilo
"""
This section of code will have the bulk of the hilo game code in it. It will take the user input, pick the random card, update the score, 
and control the output of the score.

ENH: I have renamed the file and class (Dealer) to be align to the Hilo Specifications https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""
class Dealer:

  def __init__(self):
    # We want to create a new instance of the game here and assign the Hilo class to a variable - Jordan
    
    # self.cards = [] #Is this really needed? (ENH)
    self.points = 300 #Initiates points (ENH)
    self.is_playing = True
    self.score = 0 #Points can be updated in the same points variable (ENH) ?
    self.total_score = 0 #Points can be updated in the same points variable (ENH) ?
    
    self.last_card = 0 #Variable to be used for the last card (ENH)
    self.next_card = 0 #Variable to be used for the next card (ENH)
    self.guess = '' #Variable for user selection (ENH)


    # Here we assign the Hilo class to a variable and I believe this is
    # how we would go about running it to generate the first card, not sure though. - Jordan
    #hilo = Hilo()

    self.card = Hilo() #Starts a new instance of Hilo to get a random card (ENH) to be used anywhere
  
  def start_game(self):


    #Get new card instance and assign it fo last_card
    card = self.card
    card.draw()
    self.last_card = card.value

    while self.is_playing:
      self.get_inputs()
      self.do_updates()
      self.do_outputs()


  def get_inputs(self):
    # this function allows us to ask the user if they would like to play
    # and if they say yes then we initiate the draw function from the hilo file.
    # after which we want to ask the user to guess a number and compare that
    # to the self.value integer generated via hilo.draw. - Jordan
    # draw_cards = input("Would you like to play? [y/n] ") - This could be moved to the last function instead of asking at the beggining (ENH)
    # self.is_playing = (draw_cards == "y")
    # Here we assign the random card value to a variable/ attribute and ask the player to guess higher or lower - Jordan

    print()
    print(f"The first card's number is {self.last_card}")
    self.guess = input("would you like to guess the next to be higher or lower? [h/l] ").lower()
    # If a playe inputs an invalid option it will allow them to try again
    while self.guess != "h" and self.guess != "l":
      print("\nNot a valid entry. \n")
      print(f"The first card's number is {self.last_card}")
      self.guess = input("would you like to guess the next to be higher or lower? [h/l] ").lower()



  def do_updates(self):
    if not self.is_playing:
      return

    # gets a new instance of Hilo for the next card (ENH)
    card = self.card 
    card.draw()
    self.next_card = card.value
    print(f'Next card was: {self.next_card}')


    # Compares last and next card with user selection
    if self.next_card > self.last_card and self.guess == 'h':
        self.points += 100
    elif self.next_card < self.last_card and self.guess == 'l':
        self.points += 100
    else:
        self.points -= 75

    # Updates last_card variable with the current card value for next round
    self.last_card = self.next_card



  def do_outputs(self):
    if not self.is_playing:
      return

    if self.points > 0:
        print(f'Your score is: {self.points}')
    else:
        print(f'Your score is: {self.points}')
        print('\nNo more points')
        print('Game over \n')
        self.is_playing = False
        return

    play_again = input("Play again? [y/n] ").lower()
    
    # This while statment will inform the player if that enter an incorect entry
    # It will then allow them to try again (Zack Doxey) 
    while play_again != "y" and play_again != "n":
      print("\nNot a valid entry. \n")
      play_again = input("Play again? [y/n] ").lower()
    
    self.is_playing = (play_again == "y")

    if not self.is_playing:
      print("\nThank you for playing!")
      print(f"Your final score is {self.points}\n")
