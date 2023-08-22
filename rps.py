from random import choice

# Definiujemy listę, w której piszemy po kolei każdą możliwość
list = ['rock', 'paper', 'scissors']

# Użytkownik wybiera Kamień, papier lub nożyce
userchoose = input('Choose: rock, paper, scissors ')

# Komputer wybiera z listy na górze wartość
computerchoice = choice(list)
# Dajemy if dla rock i chomputerchoice
if userchoose == "rock" and computerchoice == "rock":
    print("Double rock! No one wins.")
elif userchoose == "rock" and computerchoice == "paper":
    print("You lost! Computer chose paper.")
elif userchoose == "rock" and computerchoice == "scissors":
    print("You won! Computer chose scissors.")
# Dajemy if dla paper i chomputerchoice
elif userchoose == "paper" and computerchoice == "rock":
    print("You won! Computer chose rock.")
elif userchoose == "paper" and computerchoice == "paper":
    print("Double paper! No one wins.")
elif userchoose == "paper" and computerchoice == "scissors":
    print("You lost! Computer chose scissors.")
# Dajemy if dla rscissors i chomputerchoice
elif userchoose == "scissors" and computerchoice == "rock":
    print("You lost! Computer chose rock.")
elif userchoose == "scissors" and computerchoice == "paper":
    print("You won! Computer chose paper.")
elif userchoose == "scissors" and computerchoice == "scissors":
    print("Double scissors! No one wins.")
else:
    print("Niepoprawny wybór.")
