def rock_paper_scissors_gameplay():
    """A classic rock paper scissors game. First player to 2 wins the competition. Includes the option to play again."""
    welcome = "Welcome to Rock, Paper, Scissors. We are playing the first to 2 wins. Get ready to compete!"
    print(welcome)

    player_1_score = 0  # initialize score to 0
    player_2_score = 0  # initialize score to 0

    while player_1_score < 2 and player_2_score < 2:  # no one has reached 2 wins yet
        choices = ["rock", "paper", "scissors"]
        while True:  # Will keep running until acceptable input is given
            player_1 = input("Player 1, rock, paper or scissors?: ")
            if player_1.lower() in choices:
                break

        while True:  # Will keep running until acceptable input is given
            player_2 = input("Player 2, rock, paper, or scissors?: ")
            if player_2.lower() in choices:
                break

        if player_1.lower() == "rock":
            if player_2.lower() == "rock":
                print("It's a tie")

            elif player_2.lower() == "paper":
                print("Paper covers rock, player 2 wins this round")
                player_2_score += 1

            elif player_2.lower() == "scissors":
                print("Rock smashes scissors, player 1 wins this round")
                player_1_score += 1

        elif player_1.lower() == "paper":
            if player_2.lower() == "paper":
                print("It's a tie")

            elif player_2.lower() == "rock":
                print("Paper covers rock, player 1 wins this round")
                player_1_score += 1

            elif player_2.lower() == "scissors":
                print("Scissors cut paper, player 2 wins this round")
                player_2_score += 1

        elif player_1.lower() == "scissors":
            if player_2.lower() == "scissors":
                print("It's a tie")

            elif player_2.lower() == "paper":
                print("Scissors cut paper, player 1 wins this round")
                player_1_score += 1

            elif player_2.lower() == "rock":
                print("Rock smashes scissors, player 2 wins this round")
                player_2_score += 1

    if player_1_score == 2:
        print("Player 1 is the ultimate champion")
    elif player_2_score == 2:
        print("Player 2 is the ultimate champion")

    print("Would you like to start another competition? yes/no")
    play_again_response = input()
    if play_again_response.lower() == "yes":
        rock_paper_scissors_gameplay()
    else:
        print("Come play another time!")


rock_paper_scissors_gameplay()

