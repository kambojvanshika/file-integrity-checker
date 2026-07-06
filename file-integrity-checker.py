import hashlib

with open("test.txt", "w") as f:
    f.write("Hello World")

with open("test.txt", "rb") as f:
    data = f.read()

hash_value = hashlib.sha256(data).hexdigest()

print("File Created Successfully!")
print("SHA-256 Hash:")
print(hash_value)
