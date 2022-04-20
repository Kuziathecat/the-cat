def cart():
    a=input("Введите 16 цифр номера карты:")
    return '*' * len(a[:-4]) + a[-4:]
print(cart())




