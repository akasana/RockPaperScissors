
# coding: utf-8

# In[6]:


print("Rock Paper Scissor in Python by Abhishek Kasana")
loose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
    print("To begin fill in the below information")
    username = input("please enter your username:  ")
    password = input("please enter your password:  ")
    searchfile = open("accounts.csv", "r")
    for line in searchfile:
        if username and password in line:
            print("Access Granted")
            print("Let's play rock paper scissors")
            print("Live Rules")
            print("Yor start with", lives, "lives")
            print("If you win you get extra life")
            print("If you loose you loose a life")
            print("If you draw the lives stay the same")
            print("--------------------------------------")
            print("MAKE SURE YOU DON'T USE CAPITALS")
            print("--------------------------------------")
            print("To see the list of rules type rules")
            print("--------------------------------------")
            print("At any point type exit to leave the game")
            print("--------------------------------------")
            print("The computer has lives as well")
            print("Can you beat the computer?")
            print("Good luck!!")
            print("--------------------------------------")
            while True:
                rps = input("rock, paper, scissors?  ")
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)

                #rock if statements
                if rps == "rock" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "rock" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    computer_lives -= 1
                    score += 1

                #paper if statements
                if rps == "paper" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "paper" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    computer_lives -= 1
                    score += 1

                #scissors if statements
                if rps == "scissors" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "scissors" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    computer_lives -= 1
                    score += 1

                #duplicates
                if rps == "rock" and computer == "rock":
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1

                #system
                if rps == "rules":
                    print("*****************************")
                    print("Rules")
                    print("*****************************")
                    print("-rock looses against paper")
                    print("-rock beats scissors")
                    print("-paper looses against scissors")
                    print("-paper beats rock")
                    print("-scissors looses against rock")
                    print("-scissors beats paper")
                    print("*****************************")

                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew":
                    print(drew)

                #lives
                if lives == 0 or rps == "test":
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("press enter to exit")
                    break
                    #import time
                    #time.sleep(900)

                if computer_lives == 0:
                    print("Thanks for playing")
                    print("The computer lost all it's lives. You win.")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("press enter to exit")
                    break
                    #import time
                    #time.sleep(900)

                #exit
                if rps == "exit":
                    break

        else:
            print("Your username or password is incorrect.")
            print("---------------------------------------")
