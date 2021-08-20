import random
import os

# deal cards function
def deal_cards():
    # Ace can count as 11 or 1
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card

# calculate score function
def total_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0      
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# compare the final score
def compare_score(user_score, computer_score):
    if user_score == 0:
        return "You win!"
    elif computer_score == 0:
        return "You lose!"
    elif user_score > 21:
        return "You went over, you lose!"
    elif computer_score > 21:
        return "Opponent went over, you win!"
    elif user_score == computer_score:
        return "Draw."
    elif user_score > computer_score:
        return "You win!"
    elif user_score < computer_score:
        return "You lose!"

def game_play():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # deal 2 cards to user and computer
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # user's game
    while not is_game_over:
        user_score = total_score(user_cards)
        computer_score = total_score(computer_cards)
        print(f"Your cards: {user_cards}, current scroe:{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        # check if game is over
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Press 'y' to get another card, press 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    # computer starts the game once the user is done. Computer should keep the score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = total_score(computer_cards)

    print(f"Your final cards: {user_cards}, final scroe:{user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

while(input("Do you want to play a game? Press 'y' to play, press 'n' to end: ") == 'y'):
    os.system('cls')
    game_play()