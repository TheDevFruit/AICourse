# Git Repository: https://github.com/TheDevFruit/AICourse

num = int(input("Введите количество Рублей: "))
if num // 10 != 1 and num % 10 == 1:
    print(f"{num} рубль")
elif num // 10 != 1 and (num % 10 == 2 or num % 10 == 3 or num % 10 == 4):
    print(f"{num} рубля")
else:
    print(f"{num} рублей")
