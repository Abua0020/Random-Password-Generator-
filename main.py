import random

def generate_random_password(words):
    # Combine the input words into a single string
    combined_words = ''.join(words)

    # Convert the string into a list of characters
    characters = list(combined_words)

    # Shuffle the characters to create a random arrangement
    random.shuffle(characters)

    # Join the shuffled characters to form the final password
    password = ''.join(characters)

    return password

def main():
    print("========================Welcome to the Random Password Generator!===========================")
    print(" ")
    print("A Password for you based on your input words.")
    print("!")
    print("!")

    while True:

        # Get input words from the user
        words = input("Enter words separated by spaces (e.g., Name BirthYear): ").split()

        # Check if there are enough words for a strong password
        if len(words) < 2:
            print("Please enter at least two words for a stronger password.")
            continue

        # Generate and display the random password
        password = generate_random_password(words)
        print("Generated Password:", password)

        # Ask the user if they want to generate another password
        another_password = input("Do you want to generate another password? (yes/no): ").lower()
        if another_password != 'yes':
            print("Thank you for using the Random Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
