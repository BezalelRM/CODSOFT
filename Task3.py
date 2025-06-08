import random
import string

def generate(letter, digit, symbol):
    letters = random.choices(string.ascii_letters, k=letter)
    digits = random.choices(string.digits, k=digit)
    symbols = random.choices(string.punctuation, k=symbol)

    chars = letters + digits + symbols
    random.shuffle(chars)

    return ''.join(chars)

try:
    letter = int(input("How many letters do you want in your password? "))
    digit = int(input("How many numbers do you want? "))
    symbol = int(input("How many symbols do you want? "))

    total = letter + digit + symbol

    if total <= 0:
        print("Password must contain at least one character.")
    else:
        password = generate(letter, digit, symbol)
        print("\nYour Generated Password is:\n", password)

except ValueError:
    print("Please enter valid numbers.")
