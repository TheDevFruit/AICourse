# Git Repository: https://github.com/TheDevFruit/AICourse
# У меня старая версия пайтона - 3.9 (match не работает)
def func(text):
    match text:
        case "save":
            print("сохранить")
        case "load":
            print("сохранить")
        case _:
            print("неизвестная операция")

func(input("Введите Текст: "))
