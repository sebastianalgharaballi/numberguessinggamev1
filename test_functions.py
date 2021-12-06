from functions import opening_message, greet_player, start_game, main
import random as rand
# I tried to use monkeypatch in the last 2 functions in the same way that I did in the 2nd function.
# If incorrect, this is something I can improve on in the future!

def test_opening_message():
    assert callable(opening_message)
    assert opening_message() == 'Hello! Welcome to my number guessing game.'
    assert type(opening_message()) == str
    
def test_greet_player(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Sebastian')
    assert callable(greet_player)
    assert greet_player() == 'Sebastian'
    assert type(greet_player()) == str

def test_start_game(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'E')
    difficulty = input('Choose your number range! Type E for easy, M for medium, H for hard, or EXP for expert.')
    if difficulty.lower() == 'e':
        maximum_number = 10
        tries = 5
    number = rand.randint(0, maximum_number)
    assert callable(start_game)
    assert difficulty.lower() == 'e'
    assert maximum_number == 10
    assert tries == 5
    assert type(difficulty) == str
    assert type(number) == int
        
def test_main(monkeypatch):
    # I know that I can use the unittest Python module to test a main function.
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    play_again = input('Would you like to play again? Enter yes to continue or anything other than yes to quit.')
    while play_again.lower() == 'yes':
        correct_guesses = start_game(correct_guesses)
    stop_game = 'Thank you for playing!'
    assert callable(main)
    assert stop_game == 'Thank you for playing!'
    assert type(stop_game) == str