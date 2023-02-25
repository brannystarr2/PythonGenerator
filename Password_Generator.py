import random
import string

#The random and string modules are used to generate password consisting of lowercase letters,uppercase letters, digits and symbols
def generate_password(length):
    """Generate a random password of a given length."""
    # Define the character sets to use for the password.
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine the character sets.
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Use random.choices to select characters from the combined set.
    password = ''.join(random.choices(all_characters, k=length))

    """_summary_
" ".join() is a built-in Python method that returns a string that concatenates the items of an iterable
(e.g., list, tuple, etc.) with a given separator (in this case, a space character).
    """
    return password

password = generate_password(12)
print(password)
