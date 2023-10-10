# blackjack

My take on the Blackjack game.
First both user and the computer get 2 cards.
User has constant access to his cards, alongside with the current score, and computer's first card.
User can choose to either get another card, or pass.
Possible outcomes:
    - Draw \- user score is equal to computer score
    - Win
        - User Blackjack \- user's first 2 cards give a score of 21
        - Computer bust \- computer's score exceeds 21, but user's score is less than 21
        - Win \- both user's score and computer's score is below 21, but user's score is greater than computer's score
    - Lose
        - Computer's Blackjack \- computer's first 2 cards give a score of 21
        - User bust \- user's score exceeds 21
        - Lose \- both user's score and computer's score is below 21, but computer's score is greater than user's score