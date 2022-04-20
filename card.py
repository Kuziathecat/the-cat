def card():
    a=input("Введите 16 цифр карты: ")
    return '*' * len(a[:-4]) + a[-4:]
print(card())