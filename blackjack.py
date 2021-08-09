from blackjack_art import logo
import random
import subprocess

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def deal_card():
    return random.choice(cards)


def calculate_score(a_list):
    score = sum(a_list)
    return score


def remove_all(a_list):
    a_list.clear()


def play():

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    print(logo)
    print(f"Your cards: {user_cards}, current score :{calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}.")

    if calculate_score(user_cards) == 21:
        print(f"Your final hand: {user_cards}, final score: {calculate_score(a_list=user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(a_list=computer_cards)}")
        print(f"You win. it is Black Jack.")

    else:
        while True:
            users_choice = input("Type 'Y' to get another card, type 'N' to pass:").lower()
            if users_choice == "y":
                user_cards.append(deal_card())
                print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}.")
                print(f"Computer's first card: {computer_cards[0]}.")

                if calculate_score(user_cards) == 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}.")
                    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}.")
                    print(f"You win. it is Black Jack.")
                    break
                elif calculate_score(user_cards) > 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}.")
                    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}.")
                    print(f"You lose. it is more than 21.")
                    break
            elif users_choice == "n":
                computers_current_score = computer_cards[0]
                while True:
                    if calculate_score(computer_cards) <= 21:
                        computer_cards.append(deal_card())
                        if calculate_score(computer_cards) > calculate_score(user_cards):
                            break
                if calculate_score(computer_cards) > 21:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}.")
                    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}.")
                    print(f"You win.")
                elif calculate_score(user_cards) > calculate_score(computer_cards):
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}.")
                    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}.")
                    print(f"You win.")

                elif calculate_score(computer_cards) > calculate_score(user_cards):
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}.")
                    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}.")
                    print("You lose.")
                else:
                    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}.")
                    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}.")
                    print("No one wins.")
                break
    remove_all(user_cards)
    remove_all(computer_cards)


play()
while True:
    play_again = input("Type 'Y' to play again, type 'N' to end the game:").lower()
    if play_again == "y":
        subprocess.call("clear", shell=True)
        play()
    else:
        print("Thank you for the game")
        break
