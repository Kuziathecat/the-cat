a = input("Введите слово: ")
obr = a[::-1]
def word(s):
    while True:
        if s[::1] == obr:
            print("Является")
            break
        if s != obr:
            print("Не является")
            continue
print(word(a))
