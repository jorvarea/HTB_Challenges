# Decryption of XOR-Encrypted Message

## Introduction

In this task, we were given an encrypted message that was XORed with a 4-byte key. We also knew some information about the plaintext message, specifically that it starts with "HTB{", since all HTB flags work that way. Our goal was to decrypt the message and retrieve the original plaintext.

## Approach

### 1. Understanding XOR Encryption

XOR encryption is a symmetric key algorithm, which means the same key is used for both encryption and decryption. The XOR operation has a unique property:

\[
\text{Original} XOR \text{Key} = \text{Encrypted}
\]
\[
\text{Encrypted} XOR \text{Key} = \text{Original}
\]

This property allowed us to retrieve the original message by applying the XOR operation with the key on the encrypted message.

### 2. Finding the Key

Since we knew the message starts with "HTB{", we used this information to find the key.

1. **Convert the Encrypted Message**: We converted the encrypted message from a hexadecimal string to a byte array.
2. **Use Known Plaintext**: We XORed the known part of the plaintext "HTB{" with the corresponding part of the encrypted message to retrieve the 4-byte key: \([91, 30, 180, 154]\) or \('\x5B\x1E\xB4\x9A'\) in hexadecimal.

### 3. Decrypting the Message

With the complete key in hand, we proceeded to decrypt the entire message. We applied the XOR operation between the encrypted message and the repeating key to obtain the original plaintext.

### 4. Results and Conclusion

The decrypted message was:

\[
\text{"HTB{rep34t3d_x0r_n0t_s0_s3cu"}
\]

While the decryption was successful, the message seemed to be incomplete. But we knew that the word was secure, e are usually replaced with 3s and it must end with }. So we got the flag.

By applying a systematic approach and utilizing the properties of XOR encryption, we were able to decrypt the message and gain insights into the original content.
