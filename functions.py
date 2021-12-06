import random as rand

def opening_message():
    """Open the game with a message to the player.
    
    Returns
    -------
    message : str
        Message that welcomes the player upon entering the game.
    """

    message = 'Hello! Welcome to my number guessing game.'
    # outputting the stored message to the player
    # followed by a space for better in-game text readability
    print(message)
    print()
    
    return message

def greet_player():
    """Ask for the player's name and wish them good luck.
    
    Returns
    -------
    player_name : str
        The player's name that they input upon entering the game.
    """
    
    player_name = input('What is your name?')
    # taking the player's name and producing a statement back to them
    print()
    print('Hi', player_name, '! Good luck.')
    
    return player_name

def start_game(correct_guesses):
    """Ask the player for the difficulty of their choice and 
       begin exucution of the game.
    
    Parameters
    ----------
    correct_guesses : int
        The total number of successful guesses the player begins with (0).
        
    Returns
    -------
    correct_guesses : int
        The total number of successful guesses the player gains as they play.
    difficulty : str
        A level the user specifies that determines the numbers they guess from.
    number : int
        The random number that is generated based on difficulty.
    """
    
    print()
    # getting the player's difficulty choice 
    difficulty = input('Choose your number range! Type E for easy, M for medium, H for hard, or EXP for expert.')
    # producing range of numbers and tries based on difficulty
    if difficulty.lower() == 'e':
        print('You have 5 tries to win!')
        maximum_number = 10
        tries = 5
        
    elif difficulty.lower() == 'm':
        print('You have 8 tries to win!')
        maximum_number = 50
        tries = 8
        
    elif difficulty.lower() == 'h':
        print('You have 10 tries to win!')
        maximum_number = 100
        tries = 10
        
    elif difficulty.lower() == 'exp':
        print('You have 15 tries to win!')
        maximum_number = 1000
        tries = 15
    # accounts for the possibility of an incorrect input   
    else:
        print('You entered an incorrect input. Please restart the game and enter E, M, H, or EXP.')
        
    #randomly choosing a number based on difficulty and producing a statement   
    number = rand.randint(0, maximum_number)
    print()
    print('I know a number from 0 to ' + str(maximum_number) + '. What is this number?')
    
    attempts = 1
    # taking the player's guess
    # giving a response based on how close guess is to the random number
    # keeps track of how many attempts the player has used
    while attempts <= tries:
        
        try:
            guess = int(input('Your guess: '))
            
            if guess < number:
                print('That is too low. Try again.')
                attempts += 1
                
            elif guess > number:
                print('That is too high. Try again.')
                attempts += 1
                
            elif guess == number:
                print('Great job! You guessed it in ' + str(attempts) + ' tries.')
                correct_guesses += 1
                print('You have won', str(correct_guesses), 'games.')
                return correct_guesses
        # accounts for the possibility of an incorrect input  
        except (ValueError):
            print('Please enter an integer.')
            
            continue
            
    else:
        print('Oh no! You ran out of guesses. The number I knew was', number, '.')
        return correct_guesses
    
    return difficulty
    return number
    
def main():
    """The driver of the game that gives the player's number of correct guesses and an option to play again.
    
    Returns
    -------
    stop_game : str
        The response given to a player when they stop playing.
    """
    # initialization of functions to ensure program functionality
    # player begins game with zero correct guesses
    opening_message()
    greet_player()
    correct_guesses = 0
    play_again = 'yes'
    
    while play_again.lower() == 'yes':
    # obtaining the player's response when asked to play again
    # regenerating the game (with number of correct guesses) if they keep playing
        correct_guesses = start_game(correct_guesses)
        play_again = input('Would you like to play again? Enter yes to continue or anything other than yes to quit.')
    # terminating the game when the user does not want to play anymore   
    stop_game = 'Thank you for playing!'

    return stop_game

# test to ensure the game is executed when run as a Python program
if __name__ == '__main__':
    main()