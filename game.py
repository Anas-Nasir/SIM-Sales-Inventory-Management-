import random
def display_title():
    # Displaying the title of the game to the user
    print("Welcome to the Guessing Game")

def play_game():
    # generating the random number using python random module.
    # randint(x, y) generated random numbers that are greater than equal to x and less than equal to y '''
    target = random.randint(1, 10)
    # check for the player guess untill he guesses it right
    while True:
        player_guess = int(input("Hey guess the number"))
        if player_guess == target:
            print("You guessed It")
            break
        else:
            # if the entered number is less than the target
            if player_guess < target:
                print("Too Low")
            else:
                print("Too  High")
            continue
    # return to the main Functin
    return 

def main():
    # calling the title function to print the title
    display_title()
    var = "yes"
    # checking the var variable if it is true then call the play_game function'''
    while var == "yes":
        play_game()
        # aking the input from the user (yes or no) '''
        var = input("Do you want to play the game again: ")
    

if __name__ == "__main__":
    # Calling the main Function'''
    main()