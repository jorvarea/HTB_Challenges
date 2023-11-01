# Capture The Flag (CTF) Write-Up: ChaCha20 Cryptanalysis

## Overview

In this CTF challenge, we were provided with a Python script that utilized the ChaCha20 encryption algorithm to encrypt a known plaintext message and an unknown secret flag. Both were encrypted using the same key and Initialization Vector (IV). Our task was to decrypt and retrieve the secret flag.

## Understanding the Vulnerability

ChaCha20 is a stream cipher, and one of its crucial security practices is to never use the same key and IV pair for encrypting more than one message. The provided script, however, violated this practice by using the same key and IV for encrypting both the known plaintext message and the secret flag. This made the encryption susceptible to a "two-time pad" attack, where an attacker can XOR the ciphertexts of two messages encrypted with the same keystream to obtain the XOR of the two plaintexts.

## The Attack Strategy

Our approach to solve this challenge was based on the following steps:

1. **Extracting the Data**: We started by extracting the IV, the encrypted known plaintext message, and the encrypted flag from the "out.txt" file.

2. **Deriving the Keystream**: Since we had the plaintext and its corresponding ciphertext, we were able to derive the keystream used for encryption. This was done by performing a bitwise XOR operation between the plaintext and the ciphertext.

3. **Decrypting the Flag**: With the derived keystream in hand, we then XORed it with the encrypted flag to retrieve the original secret flag.

## Implementation

We implemented a Python script to automate the attack. The script contained functions for performing XOR operations on byte strings and for decrypting the message using the derived keystream.

## Conclusion

By exploiting the improper use of the ChaCha20 encryption algorithm (specifically, the reuse of the key and IV for multiple encryptions), we were successfully able to decrypt and retrieve the secret flag, solving the CTF challenge. This exercise underscored the importance of following cryptographic best practices, such as ensuring uniqueness of the IV for each encryption operation when using stream ciphers.
