import bcrypt

def generate_password(password: str) -> str:
    password_to_bytes=password.encode('utf-8')
    salt = bcrypt.gensalt()
    print("salt value is ",salt)
    hashed_password = bcrypt.hashpw(password=password_to_bytes,salt=salt)
    print("Hashed value of the string is : ",hashed_password)
    

print(generate_password("Nitesh1234"))
