import hashlib

class HashingAlgorithms():
    
    def sha256_encoder(string):
        string_bytes = string.encode('utf-8') # Convert the string to bytes
        sha256_hash = hashlib.sha256() # Create a SHA-256 hash object
        sha256_hash.update(string_bytes) # Update the hash object with the string bytes
        encrypted_string = sha256_hash.hexdigest() # Get the hexadecimal representation of the encrypted string

        return encrypted_string
