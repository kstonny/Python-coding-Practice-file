import sys

user1 = str(input("Player 1 Please enter your choice: "))

user2 = str(input("Player 2 Please enter your choice: "))

def compare(u1,u2):
    if u1 == u2:
        return("Its a tie")

    elif u1 == 'scissor':
        if u2 =='paper':
            return("Scissor wins")
        else:
            return("Rock wins")

    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins")
        else:
            return("Scissor wins")

    elif u1 == 'rock':
        if u2 == 'scissor':
            return("Rock wins")
        else:
            return("Paper wins")

    else:
        return("You have entered an invalid input")

print(compare(user1,user2))

sys.exit()