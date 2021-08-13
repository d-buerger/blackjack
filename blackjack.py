"""
Blackjack Game
November 20, 2019
Daniel Buerger
"""

# Imports
import random


# Constant card dictionary (Could be nested into random_card function if you wanted to avoid global variables)
CARD_DICT = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
             "Jack": 10, "Queen": 10, "King": 10, "Ace": (1, 11)}


# Method for drawing a random card - returns a random card [key, value]
def random_card():

    # Selecting a random key from the card dictionary then use that key to get its value
    random_card_selection_key = random.choice(list(CARD_DICT))
    random_card_selection_value = CARD_DICT.get(random_card_selection_key)

    return random_card_selection_key, random_card_selection_value


# Method for the dealer to draw a card until dealer_total >= 17 then return the dealer_total
def dealer_draw_and_score(first_card_name, first_card_number, second_card_name, second_card_number):

    # Ace card checks
    if first_card_name == "Ace" and second_card_name == "Ace":
        dealer_total = 12

    elif first_card_name == "Ace" and second_card_name != "Ace":
        dealer_total = first_card_number[1] + second_card_number
        if dealer_total > 21:
            dealer_total = first_card_number[0] + second_card_number

    elif first_card_name != "Ace" and second_card_name == "Ace":
        dealer_total = first_card_number + second_card_number[1]
        if dealer_total > 21:
            dealer_total = first_card_number + second_card_number[0]

    else:  # Dealer originally did not draw an ace
        dealer_total = first_card_number + second_card_number

    # Show the dealers hidden card and supply the total
    print(f"\nThe dealer reveals a hidden card of {second_card_name}. The dealers total is {dealer_total}. ")

    # Make the dealer draw a card until dealer_total >= 17
    while True:
        if dealer_total < 17:
            new_card_name, new_card_value = random_card()

            # New card Ace check and evaluate
            if new_card_name == "Ace":
                if (dealer_total + 11) < 21:  # If the dealers total + 11 is < 21 then use 11 as the value for Ace
                    dealer_total = dealer_total + new_card_value[1]
                else:  # Else use the value of 1 for Ace
                    dealer_total = dealer_total + new_card_value[0]
            else:
                dealer_total = dealer_total + new_card_value
            print(f"\nHit! The dealer draws a {new_card_name}. The dealer total is: {dealer_total}.")

        # If the dealer stands
        if dealer_total >= 17 and dealer_total < 21:
            print(f"\nThe dealer stands. The dealer total is: {dealer_total}.")
            break

        elif dealer_total > 21:  # If the dealer has a total greater than 21
            print(f"\nThe dealer busts with a total of {dealer_total}.")
            break

        elif dealer_total == 21:  # If the dealer has a total equal to 21
            break

    return dealer_total  # return the dealer_total


# Method for the determining who wins
def end_result(dealer_total, player_total):

    if dealer_total == 21:
        print(f"\nDealer has 21! Dealer Wins.")
    if player_total < 21 and dealer_total < player_total:
        print("\nPlayer wins!")
    if dealer_total < 21:
        if player_total < 21 and dealer_total > player_total:
            print("\nDealer wins!")
    if dealer_total > 21 and player_total < 21:
        print("\nPlayer wins!")
    if dealer_total == player_total:
        print("\nPush! Dealer wins!")


# Main method blackjack game
def blackjack_game():

    # First draw random cards for the player and the dealer
    player_first_card_name, player_first_card_value = random_card()
    player_second_card_name, player_second_card_value = random_card()

    dealer_first_card_name, dealer_first_card_value = random_card()
    dealer_second_card_name, dealer_second_card_value = random_card()

    # If neither of the players cards is an Ace then total the card values
    if player_first_card_name != "Ace" and player_second_card_name != "Ace":
        player_total = player_first_card_value + player_second_card_value
        print(f"\nYou draw a {player_first_card_name} and a {player_second_card_name}. Your total is: {player_total}.")

    # If the player has an Ace and a card valued at 10 then they have blackjack!
    if player_first_card_name == "Ace" or player_second_card_name == "Ace":
        if player_first_card_value == 10 or player_second_card_value == 10:
            player_total = 21
            print(f"\nYou draw a {player_first_card_name} and a {player_second_card_name}."
                  f" Your total is: {player_total}. Blackjack!")

        # Player draws an ace from the beginning but doesn't have blackjack
        else:
            print(f"\nYou draw a {player_first_card_name} and a {player_second_card_name}.")

            # Player draws two aces from the beginning
            if player_first_card_name == "Ace" and player_second_card_name == "Ace":

                # Let the player decide what total to use
                while True:
                    user_total_choice = input(f"\nPlease enter either {player_first_card_value[0] + player_second_card_value[0]}"
                                              f" or {player_first_card_value[1] + player_second_card_value[0]} as a total: ")

                    # Compare string value returned to the str value of the totals
                    if str(user_total_choice) == str(player_first_card_value[0] + player_second_card_value[0]):
                        break
                    elif str(user_total_choice) == str(player_first_card_value[1] + player_second_card_value[0]):
                        break
                    else:
                        continue

                player_total = int(user_total_choice)  # Convert back to int data type


            # Players first card drawn is an Ace
            elif player_first_card_name == "Ace":

                # Let the player decide what total to use
                while True:
                    user_total_choice = input(f"\nPlease enter either {player_first_card_value[0] + player_second_card_value}"
                                              f" or {player_first_card_value[1] + player_second_card_value} as a total: ")

                    # Compare string value returned to the str value of the totals
                    if str(user_total_choice) == str(player_first_card_value[0] + player_second_card_value):
                        break
                    elif str(user_total_choice) == str(player_first_card_value[1] + player_second_card_value):
                        break
                    else:
                        continue

                player_total = int(user_total_choice)


            # Players second card drawn is an Ace
            else:

                # Let the player decide what total to use
                while True:
                    user_total_choice = input(f"\nPlease enter either {player_first_card_value + player_second_card_value[0]}"
                                              f" or {player_first_card_value + player_second_card_value[1]} as a total: ")

                    # Compare string value returned to the str value of the totals
                    if str(user_total_choice) == str(player_first_card_value + player_second_card_value[0]):
                        break
                    elif str(user_total_choice) == str(player_first_card_value + player_second_card_value[1]):
                        break
                    else:
                        continue

                player_total = int(user_total_choice)


            # Print initial player total
            print(f"\nYour total is: {player_total}")

    # Print the dealers first card name
    print(f"\nThe dealer draws a {dealer_first_card_name} and a hidden card.")

    # Allow the player to double down on the first hit/stand opportunity (Hint: Always double down on an 11 !)
    offer_to_double = True

    # Running loop for the blackjack game
    while True:

        # If the players total is 21 then stand for the player and draw for the dealer, dealer wins 21 tie
        if player_total == 21:

            dealer_total = dealer_draw_and_score(dealer_first_card_name, dealer_first_card_value,
                                                 dealer_second_card_name, dealer_second_card_value)

            # See who won the game
            if dealer_total == 21:
                print(f"\nDealer has 21! Dealer Wins")
            if dealer_total < 21:
                print("\nPlayer wins!")
            if dealer_total > 21:
                print("\nPlayer wins!")

            break

        # If the player has a total less than 21 offer a choice (h/s/d)
        elif player_total < 21:

            # Offer to double will only be true on first pass of while loop
            if offer_to_double == True:
                choice_1 = input("\nHit or stand or double down? (h/s/d): ")
                choice_2 = ""
            else:
                choice_1 = ""
                choice_2 = input("\nHit or stand? (h/s): ")


            # Player decides to hit, draw a card and evaluate the players total
            if choice_1 == "h" or choice_2 == "h":

                new_card_name, new_card_value = random_card()

                # Player draws an Ace
                if new_card_name == "Ace":
                    if (player_total + 11) <= 21:  # Player can choose what total they have if their total + 11 is less than 21

                        # Loop for the player to decide their total score
                        while True:
                            user_hit_total_choice = input(f"\nYou draw an Ace, Please enter either {player_total + 1} or"
                                                          f" {player_total + 11} as a total: ")

                            # Comparing the string value the user entered for the score
                            if str(user_hit_total_choice) == str(player_total + 11):
                                break
                            elif str(user_hit_total_choice) == str(player_total + 1):
                                break
                            else:
                                continue

                        player_total = int(user_hit_total_choice)  # Convert back to int data type

                    else:  # Else the player is forced to use the Ace card as a value of 1
                        player_total = player_total + new_card_value[0]
                        print(f"\nYou draw a Ace. Your total is {player_total}")

                # Player doesn't draw an Ace, add the newly drawn card value to the running total
                else:
                    player_total = player_total + new_card_value
                    print(f"\nYou draw a {new_card_name}. Your total is {player_total}")

                # Set double down offer to False after first pass
                offer_to_double = False

                continue


            # Player decides to stand with their total
            if choice_1 == "s" or choice_2 == "s":

                print(f"\nYou choose to stand with a total of {player_total}.")

                # Draw for the dealer until the dealer has a total of 17 or over
                dealer_total = dealer_draw_and_score(dealer_first_card_name, dealer_first_card_value,
                                                     dealer_second_card_name, dealer_second_card_value)

                # See who won the game
                end_result(dealer_total, player_total)

                break
                
                
            # Player decides to double down on the first hand
            if choice_1 == "d":

                print(f"\nYou choose to double down!.")

                new_card_name, new_card_value = random_card()  # Draw a card

                if new_card_name == "Ace":  # If the card is an ace, automatically assign the player their best possible total
                    if (player_total + 11) < 21:
                        player_total = player_total + new_card_value[1]
                    else:
                        player_total = player_total + new_card_value[0]

                else:  # Card isn't an ace, total the players score with the new card value
                    player_total = player_total + new_card_value

                print(f"\nYou draw a {new_card_name}. Your total is {player_total}.")

                if player_total > 21:  # Player goes over 21 from drawing a double down card
                    print("\nSorry. You went over 21. Player loses.")

                    break

                # Draw for the dealer until the dealer has a total of 17 or over
                dealer_total = dealer_draw_and_score(dealer_first_card_name, dealer_first_card_value,
                                                     dealer_second_card_name, dealer_second_card_value)

                # See who won the game
                end_result(dealer_total, player_total)

                break


        # If player goes over 21 from taking a card (hit)
        elif player_total > 21:
            print(f"\nYou went over 21. Player loses!")

            break

# Main control method for game flow
def main():

    print("\nWelcome to Blackjack! -Program created by Daniel Buerger 2019")  # Greeting message
    print(f"\n{'-'*50}")

    # Main game loop
    while True:

        # Ask user if they want to start a new game or exit
        new_game = input("\n\nDo you wish to start a new game? (y/n):")

        if new_game == "y":
            blackjack_game()  # Run the blackjack game method
            print(f"\n{'-' * 50}")

        elif new_game == "n":
            print("\n\nThanks for playing!\n\n")
            break


if __name__ == "__main__":
    main()