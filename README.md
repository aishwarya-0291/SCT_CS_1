# Caesar Cipher CLI Tool

A simple, interactive command-line interface (CLI) application written in Python that encrypts and decrypts text using the classic **Caesar Cipher** algorithm. 

This project demonstrates core programming concepts such as modular arithmetic, string manipulation, user input validation, and loop structures.



## How It Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. For example, with a shift of `3`:
* `A` becomes `D`
* `B` becomes `E`
* `Z` wraps around to become `C`

### Mathematical Formula
* **Encryption:** $$E_n(x) = (x + n) \pmod{26}$$
* **Decryption:** $$D_n(x) = (x - n) \pmod{26}$$

*(Where $x$ is the alphabet position 0-25, and $n$ is the shift value).*

## Features

* **Dual Modes:** Easily switch between Encryption and Decryption modes.
* **Case Preservation:** Maintains lowercase and uppercase structure perfectly.
* **Symbol & Space Immunity:** Keeps spaces, numbers, and punctuation exactly as they are.
* **Input Validation:** Prevents program crashes by handling invalid character shifts gracefully.
* **Infinite Execution Loop:** Keep encrypting/decrypting multiple messages until you choose to quit.


