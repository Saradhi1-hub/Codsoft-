import random

options = ['rock', 'paper', 'scissors']

print("🎮 Rock - Paper - Scissors Game 🎮")
print("Type 'exit' to quit\n")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing! 👋")
        break
    elif user_choice not in options:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    print()
      
