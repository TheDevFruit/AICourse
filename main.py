# Git Repository: https://github.com/TheDevFruit/AICourse

text = str(input("Введите Текст: "))
count = 0
for i in range(len(text)):
    if text[i].lower() == "к" and i < len(text)-2:
         if text[i] + text[i+1] + text[i+2] in ["Кот", "КОТ", "кот"]:
             count += 1
print(count)
