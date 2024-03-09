def dictionary_attack(password):
    # Open the dictionary file
    with open('dictionary.txt', 'r') as f:
        # Read each line (password) from the dictionary
        for line in f:
            # Strip newline character and whitespace
            attempt = line.strip()
            # Check if the current password attempt matches the target password
            if attempt == password:
                print(f"Password cracked! The password is: {attempt}")
                return True
    # If no match is found
    print("Password not found in the dictionary.")
    return False

# Example usage
target_password = input("Enter the target password: ")
dictionary_attack(target_password)
