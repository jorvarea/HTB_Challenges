from binascii import unhexlify

def xor_decrypt(encrypted_message, key):
    """Decrypt a message that has been XORed with a key."""
    return bytes(a ^ b for a, b in zip(encrypted_message, key * (len(encrypted_message) // len(key))))

def main():
    # Encrypted message (in hexadecimal)
    encrypted_message_hex = "134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"
    
    # Convert the encrypted message to bytes
    encrypted_message = unhexlify(encrypted_message_hex)
    
    # Known start of the flag
    known_plaintext = "HTB{"
    
    # Convert the known plaintext to bytes
    known_plaintext_bytes = known_plaintext.encode()
    
    # Find the 4-byte key by XORing the known plaintext with the encrypted message
    key = bytes(a ^ b for a, b in zip(known_plaintext_bytes, encrypted_message[:4]))
    
    # Decrypt the entire message using the key
    decrypted_message = xor_decrypt(encrypted_message, key)
    
    # Convert the decrypted message to a string
    decrypted_message_str = decrypted_message.decode('utf-8', errors='replace')
    
    # Print the decrypted message
    print("Decrypted Message:", decrypted_message_str)

if __name__ == "__main__":
    main()
