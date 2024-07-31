import random

def print_choice(choice):
  """Prints the corresponding text-based image for the given choice."""
  if choice == "r":
    print(r)
  elif choice == "p":
    print(p)
  elif choice == "s":
    print(s)

def determine_winner(user_choice, computer_choice):
  """Determines the winner of the game."""
  if user_choice == computer_choice:
    return "It's a tie!"
  elif user_choice == "r":
    if computer_choice == "s":
      return "You win! Rock smashes scissors."
    else:
      return "You lose! Paper covers rock."
  elif user_choice == "p":
    if computer_choice == "r":
      return "You win! Paper covers rock."
    else:
      return "You lose! Scissors cuts paper."
  elif user_choice == "s":
    if computer_choice == "p":
      return "You win! Scissors cuts paper."
    else:
      return "You lose! Rock smashes scissors."

def play():
  """Main game loop."""
  print("Welcome to Rock, Paper, Scissors!")

  while True:
    user_choice = input("Enter your choice (r, p, s): ").lower()
    if user_choice not in ["r", "p", "s"]:
      print("Invalid choice. Please try again.")
      continue

    computer_choice = random.choice(["r", "p", "s"])

    print("\nYou:")
    print_choice(user_choice)

    print("\nComputer:")
    print_choice(computer_choice)

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
      break

# Text-based images for rock, paper, scissors
r =''' 
        _________
     ---'     _____)
             (________)         
             (______)
     ---,___(____)    
     '''
p = '''
        --------
     ---' _____) ____
               ________)
              __________)
               ________)
    ---,____________)
    '''
s = '''
          -------
     ---' ______)____
          __________)
          _____________)
          (_____)
    ---,__(___)
'''
game_images = [r, p, s]

play()
