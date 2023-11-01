# RSA Encryption Vulnerability Exploitation Write-up

## Overview
In this write-up, we will detail a method to decrypt an RSA encrypted message when both the key length is short, and a low public exponent is used, exploiting the mathematical properties of RSA to retrieve the original plaintext.

## RSA Basics
RSA encryption is a type of public key cryptography that utilizes two keys: a public key for encryption and a private key for decryption. The security of RSA is based on the practical difficulty of factoring the product of two large prime numbers.

A public key is made of two numbers: \( n \) and \( e \). The number \( n \) is the product of two prime numbers \( p \) and \( q \), and \( e \) is the public exponent. The private key is made of \( n \) and \( d \), where \( d \) is the modular multiplicative inverse of \( e \) modulo \( \phi(n) \) (Euler's totient function of \( n \)).

The encryption of a plaintext message \( m \) is done using the formula: 
\[ c \equiv m^e \mod n \]

And the decryption uses:
\[ m \equiv c^d \mod n \]

## The Vulnerability
The vulnerability arises when a short message and a low public exponent are used. This can lead to situations where \( m^e < n \), making it possible to directly compute the e-th root of the ciphertext to retrieve the plaintext.
