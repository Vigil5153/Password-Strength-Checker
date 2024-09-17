
# 🔒 Password Strength Checker

A Python-based tool designed to evaluate the strength of passwords, check for breaches via the **Have I Been Pwned** API, and generate secure passwords. This tool provides real-time feedback and suggests improvements for weak passwords, making it a useful tool for securing accounts.

---

## 🚀 Features

- **Password Strength Evaluation**: Analyzes passwords based on length, character variety, and common weaknesses.
- **Entropy Calculation**: Measures the randomness of a password using entropy.
- **API Integration**: Utilizes the **Have I Been Pwned** API to check if a password has been involved in data breaches.
- **Password Generation**: Creates highly secure passwords based on customizable length and character types.
- **Color-Coded CLI**: Provides real-time feedback in an interactive command-line interface with colored messages.

---

## ⚙️ Installation

To install and run the tool on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vigil5153/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

Run the tool and select the desired option:

1. **Start the Program**:
   ```bash
   python password_checker.py
   ```

2. **Choose an Option**:
   - **Check Password Strength**: Enter a password to evaluate its security level.
   - **Generate Strong Password**: Let the tool generate a secure password based on your preferred length.
   - **Exit**: Close the program when you're done.

---

## 📊 Example Output

When checking a password's strength, the tool provides a detailed breakdown, as shown below:

```bash
Enter a password to check its strength: MySecurePassword123!
Password Strength: Strong
Entropy: 76.14 bits
- Your password is secure, but consider adding more symbols for extra strength.
```

For password generation:

```bash
Generated Password: @!5LcH$9i2T#
Note: Remember to store your password securely!
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

## 🤝 Contributions

Contributions are always welcome! If you discover bugs or have ideas for improvements, please open an issue or submit a pull request. Let’s work together to make password security stronger for everyone.
