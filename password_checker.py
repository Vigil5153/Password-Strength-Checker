import re
import math
import requests
import hashlib
import secrets
import string
from colorama import Fore, Style, init

init(autoreset=True)

# functions for password checking
def calculate_entropy(password):
    unique_chars = set(password)
    pool_size = 0

    if any(c.islower() for c in unique_chars):
        pool_size += 26
    if any(c.isupper() for c in unique_chars):
        pool_size += 26
    if any(c.isdigit() for c in unique_chars):
        pool_size += 10
    if any(c in string.punctuation for c in unique_chars):
        pool_size += len(string.punctuation)

    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    return entropy

def check_pwned_api(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        hashes = (line.split(':') for line in response.text.splitlines())
        return any(tail == h for h, count in hashes)
    except requests.RequestException as e:
        print(f"{Fore.RED}[Error] Could not check Pwned API: {e}")
        return False

def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            return password

def check_password_strength(password):
    # Criteria
    criteria = {
        'length': len(password) >= 12,
        'digits': bool(re.search(r'\d', password)),
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'symbols': bool(re.search(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/~`-]', password)),
    }

    entropy = calculate_entropy(password)
    pwned = check_pwned_api(password)

    # Scoring logic
    score = sum(criteria.values())
    if entropy >= 80 and score >= 5 and not pwned:
        strength = f"{Fore.GREEN}Very Strong"
    elif entropy >= 60 and score >= 4 and not pwned:
        strength = f"{Fore.YELLOW}Strong"
    elif entropy >= 40 and score >= 3:
        strength = f"{Fore.BLUE}Medium"
    else:
        strength = f"{Fore.RED}Weak"

    # Print feedback
    print(f"\nPassword Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits\n")

    if pwned:
        print(f"{Fore.RED}- Your password has been exposed in a data breach.")

    if strength != "Very Strong":
        print(f"{Fore.YELLOW}\nTips to improve your password:")
        if not criteria['length']:
            print("- Use at least 12 characters.")
        if not criteria['digits']:
            print("- Include digits.")
        if not criteria['uppercase']:
            print("- Include uppercase letters.")
        if not criteria['lowercase']:
            print("- Include lowercase letters.")
        if not criteria['symbols']:
            print("- Include special symbols.")
        if pwned:
            print("- Avoid using passwords that have been compromised.")
        print("- Use a mix of character types for higher entropy.")

def main():
    while True:
        print(f"\n{Fore.CYAN}Password Strength Checker")
        print(f"{Fore.CYAN}1. Check Password Strength")
        print(f"{Fore.CYAN}2. Generate Strong Password")
        print(f"{Fore.CYAN}3. Exit")
        choice = input(f"{Fore.WHITE}Select an option: ")

        if choice == '1':
            pwd = input("Enter a password to check its strength: ")
            check_password_strength(pwd)
        elif choice == '2':
            length = input("Enter desired password length (default 16): ")
            length = int(length) if length.isdigit() else 16
            new_password = generate_strong_password(length)
            print(f"\n{Fore.GREEN}Generated Password: {new_password}")
            print("Note: Remember to store your password securely.")
        elif choice == '3':
            print(f"{Fore.CYAN}Exiting Password Strength Checker.")
            break
        else:
            print(f"{Fore.RED}Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
