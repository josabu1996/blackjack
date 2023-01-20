from py_d11_blackjack_logo import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
your_cards = []
status = True
continue_game = True

def you(your_cards):
    your_cards.append(random.choice(cards))

def dealer(dealer_cards):
    dealer_cards.append(random.choice(cards))

def your_card_sum(your_cards):
    return sum(your_cards)

def dealer_card_sum(dealer_cards):
    return sum(dealer_cards)

def dealer_decision(dealer_cards):
    if dealer_card_sum(dealer_cards) <= 16:
        while dealer_card_sum(dealer_cards) <= 16:
            dealer_cards.append(random.choice(cards))

def score_display(your_cards,dealer_cards):
    print(f"Your cards: {your_cards}, current score: {your_card_sum(your_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

def final_score_display(your_cards,dealer_cards):
    print(f"Your final hand: {your_cards}, final score: {your_card_sum(your_cards)}")
    print(f"Dealer's final card: {dealer_cards}, final score: {dealer_card_sum(dealer_cards)}")

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play_game == 'y':
    print(logo)
    for i in range(0, 2):
        you(your_cards)
        dealer(dealer_cards)
    dealer_decision(dealer_cards)

    score_display(your_cards, dealer_cards)
    while continue_game == True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            your_cards.append(random.choice(cards))
            if your_card_sum(your_cards) > 21:
                final_score_display(your_cards, dealer_cards)
                print("You went over. You lose 😤")
            else:
                score_display(your_cards, dealer_cards)
        elif another_card == 'n':
            if dealer_card_sum(dealer_cards) == your_card_sum(your_cards):
                final_score_display(your_cards, dealer_cards)
                print("It's a draw 😤")
            elif dealer_card_sum(dealer_cards) > 21 and your_card_sum(your_cards) <= 21:
                final_score_display(your_cards, dealer_cards)
                print("Opponent went over. You win 😁")
            elif dealer_card_sum(dealer_cards) <= 21 and dealer_card_sum(dealer_cards) > your_card_sum(your_cards):
                final_score_display(your_cards, dealer_cards)
                print("You lose 😤")
            elif your_card_sum(your_cards) <= 21 and dealer_card_sum(dealer_cards) < your_card_sum(your_cards):
                final_score_display(your_cards, dealer_cards)
                print("You win 😁")
            continue_game = False