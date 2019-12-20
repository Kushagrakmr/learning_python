var1 = input("Enter Your Choice:\nPlayer 1  ").lower()
print("No Cheating !\n" * 20)

var2 = input("Enter Your Choice:\nPlayer 2  ").lower()

if var1 == var2:
    print("It's a draw.")
elif var1 == "scissor" and var2 == "paper":
    print("Player 1 Wins!")
elif var1 == "paper" and var2 == "rock":
    print("Player 1 Wins!")
elif var1 == "rock" and var2 == "scissor":
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")