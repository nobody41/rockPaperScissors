import random


def rock_paper_scissors():
    weapon = "rock", "paper", "scissors"
    player = input("Choose: rock, paper or scissors: ")
    enemy = random.choice(weapon)
    if player == enemy:
        print("Draw!")
        rock_paper_scissors()
    if player == "rock":
        if enemy == "paper":
            print("You LOSE, enemy choose paper")
        elif enemy == "scissors":
            print("You WIN, enemy choose scissors")
    elif player == "paper":
        if enemy == "scissors":
            print("You LOSE, enemy choose scissors")
        elif enemy == "rock":
            print("You WIN, enemy choose rock")
    elif player == "scissors":
        if enemy == "rock":
            print("You LOSE, enemy choose rock")
        elif enemy == "paper":
            print("You WIN, enemy choose paper")
    else:
        print("---ErR0r---")
        print("Try again!")
        rock_paper_scissors()


rock_paper_scissors()
