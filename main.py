# Git Repository: https://github.com/TheDevFruit/AICourse

def first_letter(x):
    return x[0]


arr = ['Иван', 'Алиса', 'Петр', 'Ольга', 'Евгения', 'Дмитрий', 'Ли']
arr.sort(key=first_letter)
for i in range(len(arr)): print(f"{i} {arr[i]}")
