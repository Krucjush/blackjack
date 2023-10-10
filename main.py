import os
import art
import random

def clean():
    """clears the console"""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.name('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = True

while play:
    clean()
    print(art.logo)
    game_over = False

    def deal_card():
        """Returns a random value from the cards list"""
        return random.choice(cards)

    user_cards = []
    computer_cards = []


    for number in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        """Takes a list as an input
        Returns 0 if a Blackjack occured
        Else returns sum of values in an array"""
        score = sum(cards)
        if len(cards) == 2 and score == 21:
            return 0
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
    def state():
        """Prints current state of user cards and score alongside with computer's first card"""
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
    
    state()

    while not game_over:
        if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:
            game_over = True
        elif input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            user_cards.append(deal_card())
            state()
        else:
            game_over = True

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    def compare(user_score, computer_score):
        """Takes user score and computer score as input
        Returns a flag for what was the outcome, and why"""
        if user_score == computer_score:
            return 'draw'
        elif user_score == 0:
            return 'user_blackjack'
        elif computer_score == 0:
            return 'computer_blackjack'
        elif user_score > 21:
            return 'user_bust'
        elif computer_score <= 21 and computer_score > user_score and user_score <= 21:
            return 'lose'
        elif user_score <= 21 and user_score > computer_score and computer_score <= 21:
            return 'win'
        elif user_score <= 21 and computer_score > 21:
            return 'computer_bust'
        
    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

    result = compare(calculate_score(user_cards), calculate_score(computer_cards))
    if result == 'draw':
        print('Draw')
    elif result == 'win':
        print('You win')
    elif result == 'user_blackjack':
        print('You win to a Blackjack')
    elif result == 'computer_blackjack':
        print('You lose to a computer Blackjack')
    elif result == 'computer_bust':
        print('You win to a computer bust')
    else:
        print('You lose')
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'y':
        play = False