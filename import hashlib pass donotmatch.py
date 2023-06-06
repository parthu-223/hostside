import hashlib

password1 = input("Enter password 1: ")
password2 = input("Enter password 2: ")

# Hash the passwords using SHA256 algorithm
hash1 = hashlib.sha256(password1.encode()).hexdigest()
hash2 = hashlib.sha256(password2.encode()).hexdigest()

if hash1 == hash2:
    print("Passwords match")
else:
    print("Passwords do not match")
