from py_d11_blackjack_logo import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
your_cards = []
status = True

def you(your_cards):
    your_cards.append(random.choice(cards))

def dealer(dealer_cards):
    dealer_cards.append(random.choice(cards))

def your_card_sum(your_cards):
    return sum(your_cards)

def dealer_card_sum(dealer_cards):
    return sum(dealer_cards)

def final_decision(your_cards,dealer_cards):
    if dealer_card_sum(dealer_cards) > 21:
        print(f"Your final hand: {your_cards}, final score: {your_card_sum(your_cards)}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_card_sum(dealer_cards)}")
        print("You win 😃")
        exit()
    elif dealer_card_sum(dealer_cards) <= 21 and dealer_card_sum(dealer_cards) > your_card_sum(your_cards):
        print(f"Your final hand: {your_cards}, final score: {your_card_sum(your_cards)}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_card_sum(dealer_cards)}")
        print("You lose 😭")
        exit()
    elif dealer_card_sum(dealer_cards) == your_card_sum(your_cards):
        print(f"Your final hand: {your_cards}, final score: {your_card_sum(your_cards)}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_card_sum(dealer_cards)}")
        print("Draw 😤")
        exit()

def dealer_decision(your_cards,dealer_cards):
    while dealer_card_sum(dealer_cards) <= 21:
        if your_card_sum(your_cards) == dealer_card_sum(dealer_cards):
            final_decision(your_cards,dealer_cards)
        elif dealer_card_sum(dealer_cards) > your_card_sum(your_cards):
            final_decision(your_cards,dealer_cards)
        elif dealer_card_sum(dealer_cards) < your_card_sum(your_cards):
            dealer(dealer_cards)
            final_decision(your_cards, dealer_cards)
    print(dealer_cards)
    print(dealer_card_sum(dealer_cards))


#Initial Round
print(logo)
for i in range(0,2):
    you(your_cards)
    dealer(dealer_cards)

print(f"Your cards: {your_cards}, current score: {your_card_sum(your_cards)}")
print(f"Dealer's first card: {dealer_cards[0]}")

while status == True:
    another_card = input("Type 'y' for draw again, type 'n' to stand: ").lower()
    if another_card == 'y':
        you(your_cards)
        if your_card_sum(your_cards) > 21:
            print(f"Your final hand: {your_cards}, final score: {your_card_sum(your_cards)}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_card_sum(dealer_cards)}")
            print("You lose 😭")
        else:
            print(f"Your cards: {your_cards}, current score: {your_card_sum(your_cards)}")

    elif another_card == 'n':
        if dealer_card_sum(dealer_cards) > 21:
            print(f"Your final hand: {your_cards}, final score: {your_card_sum(your_cards)}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_card_sum(dealer_cards)}")
            print("You lose 😭")
        else:
            dealer_decision(your_cards,dealer_cards)