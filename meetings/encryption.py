def encrypt_email(email: str, shift: int) -> str:
    encrypted_email = ""

    for char in email:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                encrypted_email += chr((ord(char) + shift - 65) % 26 + 65)
            # Handle lowercase letters
            else:
                encrypted_email += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave non-alphabetic characters unchanged (e.g., @, ., etc.)
            encrypted_email += char

    return encrypted_email

def decrypt_email(encrypted_email: str, shift: int) -> str:
    decrypted_email = ""

    for char in encrypted_email:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                decrypted_email += chr((ord(char) - shift - 65) % 26 + 65)
            # Handle lowercase letters
            else:
                decrypted_email += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Leave non-alphabetic characters unchanged
            decrypted_email += char

    return decrypted_email

# Example usage
email = "example@example.com"
shift = 3  # You can change the shift value

encrypted_email = encrypt_email(email, shift)
print(f"Encrypted Email: {encrypted_email}")

decrypted_email = decrypt_email(encrypted_email, shift)
print(f"Decrypted Email: {decrypted_email}")
