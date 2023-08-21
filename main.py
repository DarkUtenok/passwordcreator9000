import random

simbols = "1234567890-+_+qwertyuiop\asdfghjkl;'zxcvbnm,./!@#$%^&*😭🥺😨😫😔😟😈🥚😤👿👋🤓🧐🥶🤔🤯🤐🕶️🫥👛🍄😬🥱🍕1957"

password_length = int(input("введите длинну пароля: "))

generated_password = ""

for i in range(password_length):
    generated_password += random.choice(simbols)

print(generated_password)
