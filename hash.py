import bcrypt

def generate_password(password: str) -> str:
    password_to_bytes=password.encode('utf-8')
    salt = bcrypt.gensalt()
    # print("salt value is ",salt)
    hashed_password = bcrypt.hashpw(password=password_to_bytes,salt=salt)
    # print("Hashed value of the string is : ",hashed_password)

    return hashed_password.decode("utf-8")

# print(generate_password("Nitesh1234"))


def check_password(plain_text,hashed_value) -> bool : 
    plain_password_to_bytes = plain_text.encode('utf-8')
    hashed_value_to_byte = hashed_value.encode('utf-8')
    return (bcrypt.checkpw
            (password=plain_password_to_bytes,
            hashed_password=hashed_value_to_byte))

print(check_password("Nitesh1234","$2b$12$E.pxaa9nqYyJZIX4A7vyXeehm8gk18udcSKeKY0FyshVnIFQ/845e"))