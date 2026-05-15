def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            # (ASCII_value - 65 + shift) % 26 + 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            # (ASCII_value - 97 + shift) % 26 + 97
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave non-alphabetical characters (spaces, punctuation) as they are
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Program ---")
    
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue
            
        message = input("Enter your message: ")
        
        # Ensure the user enters a valid integer for the shift
        while True:
            try:
                shift = int(input("Enter shift value (integer): "))
                break
            except ValueError:
                print("Please enter a valid whole number.")
        
        if choice == 'E':
            encrypted_message = caesar_cipher(message, shift, mode='encrypt')
            print(f"\nEncrypted Message: {encrypted_message}\n")
        elif choice == 'D':
            decrypted_message = caesar_cipher(message, shift, mode='decrypt')
            print(f"\nDecrypted Message: {decrypted_message}\n")

if __name__ == "__main__":
    main()