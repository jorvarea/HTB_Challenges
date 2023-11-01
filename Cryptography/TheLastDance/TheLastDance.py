from Crypto.Cipher import ChaCha20

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def decrypt_message(known_plaintext, known_ciphertext, target_ciphertext):
    # Calculate the keystream used for encryption
    keystream = xor_bytes(known_plaintext, known_ciphertext)
    
    # Use the keystream to decrypt the target ciphertext
    decrypted_flag = xor_bytes(keystream, target_ciphertext)
    return decrypted_flag

if __name__ == "__main__":
    # Assume these values are extracted from the 'out.txt' file
    iv = bytes.fromhex('c4a66edfe80227b4fa24d431')
    encrypted_message = bytes.fromhex('7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990')
    encrypted_flag = bytes.fromhex('7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7')

    # The known plaintext message (must be the exact same length as the encrypted message)
    known_message = b"Our counter agencies have intercepted your messages and a lot "
    known_message += b"of your agent's identities have been exposed. In a matter of "
    known_message += b"days all of them will be captured"

    # Decrypt the flag using the known message, encrypted message, and encrypted flag
    decrypted_flag = decrypt_message(known_message, encrypted_message, encrypted_flag)
    print("Decrypted Flag:", decrypted_flag)
